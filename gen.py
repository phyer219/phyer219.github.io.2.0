from xml.sax.handler import ContentHandler
from xml.sax import parse
from zqwblog.renderer.core import OrgPost, MdPost
import os
import shutil
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler

SOURCE_PATH = './source/'
THEME_PATH = './themes/bisque/out/'
OUTPUT_PATH = './docs/'


def clean_dir(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


class PostsList:
    def __init__(self, source_path, output_path, theme_path):
        """Read the source file of the website, 
           use the theme file, generate all the static html.

        Args:
            posts_path (str): the path where the posts soure file saved
            output_path (str): the root of the website
            theme_path (_type_): the path of the theme file

        source_path should be as:
        source_path---------------
                     |-posts
                     |-about--index.md
                     |------------

        theme_path should be as:
        theme_path--------------
                   |-
        """
        self.source_path = source_path
        self.output_path = output_path
        self.theme_path = theme_path
        self.load_theme()
        self.init_output()
        self.item_list = []

    def run(self):
        """
        steps to generate all blog:

        -> 
        scan_posts(): read all post source files, into a list self.item_list
        ->
        gen_index():
        ->
        gen_categories():
        ->
        gen_about():
        """
        self.scan_posts()
        self.gen_index()
        self.gen_categories()
        self.gen_about()

    def init_output(self):
        """
        ->
        clean the output_path (now suppose the output_path has already exists)
        ->
        copy the static file in theme to the output path
        ->
        generate the directories where the output file saves.
        ->
        generate CNAME
        """
        clean_dir(self.output_path)
        shutil.copytree(self.theme_path + 'static', self.output_path + 'static')
        os.mkdir(self.output_path + 'posts')
        os.mkdir(self.output_path + 'category')
        with open (self.output_path + 'CNAME', 'w') as f:
            f.write('zqw.ink')

    def load_theme(self):
        """load the theme files.
        """
        with open(self.theme_path + 'posts/post.html', 'r') as f:
            self.post_theme = f.read()
        with open(self.theme_path + 'index.html', 'r') as f:
            self.index_theme = f.read()
        with open(self.theme_path + 'category/category.html', 'r') as f:
            self.category_theme = f.read()

    def scan_posts(self):
        """
        ->
        scan the post source file directory
        ->
        render it!
        ->
        generate a Post list
        ->
        sort it by date
        """
        posts_source = self.source_path + 'posts/'
        dir_list = os.listdir(posts_source)
        for p in dir_list:
            if os.path.isfile(posts_source + p):
                (file_root, file_extension) = os.path.splitext(p)
                if file_extension in ('.org', '.md'):
                    post = self.render_post(file_root, file_extension)
                    self.item_list.append(post)
        self.item_list.sort(key=lambda p: (p.meta['date'][0]), reverse=True)

    
    def render_post(self, file_root, file_extension):
        """According the file type, use different render,
           render it and generate the html file,
           finaly return a Post

        Args:
            file_root (_str_): post file name with extension
            file_extension (_str_): extension
            for example:
                file_root = "2020-05-18-physics-Functional"
                file_extension = "org"

        Raises:
            RuntimeError: unsuported post source file type
        """
        post_source = self.source_path + 'posts/' + file_root + file_extension
        if file_extension == '.org':
            post = OrgPost(post_source)
        elif file_extension == '.md':
            post = MdPost(post_source)
        else:
            raise RuntimeError(f'unsupported soure file type: {post_source:s}')
        post.gen_html()
        self.gen_post_page(post)
        return post

    def gen_index(self):
        with open(self.output_path + 'index.html', 'w') as f:
            for line in self.index_theme.splitlines():
                if re.search(r'{post-url}', line):
                    for post in self.item_list:
                        new_line = self.post_link(line, post)
                        f.writelines(new_line)
                else:
                    f.writelines(line)

    def post_link(self, link_theme, post, link_base='./'):
        """create a link html
        
        link_theme = "...{post-url}...{post-title}...{post-date}"
        ==>
        return link_html = "...path...title...xxxx.x.x" (e.g. 2020.1.1)
        """
        post_url =  link_base + 'posts/' + post.file_root + '.html'
        link_html = link_theme.replace(r'{post-url}', post_url)
        link_html = link_html.replace(r'{post-title}', post.meta['title'][0])
        date = '.'.join([str(i) for i in post.meta['date']])
        link_html = link_html.replace(r'{post-date}', date)
        return link_html

    def gen_post_page(self, post, export_to='posts/'):
        """input a Post, using theme to generate a html file"""
        html = self.post_theme.replace(r'{main}', post.html)
        html = html.replace(r'{title}', post.meta['title'][0])
        date = '.'.join([str(i) for i in post.meta['date']])
        html = html.replace(r'{post-date}', date)
        if 'tags' in post.meta.keys():
            html = html.replace(r'{post-tags}', str(post.meta['tags']))
        html = html.replace(r'{post-category}', str(post.meta['categories'][0]))

        with open(self.output_path + export_to
                  + post.file_root + '.html', 'w') as f:
            f.write(html)
        self.move_post_dir(post)

    def gen_about(self):
        """generate about file"""
        os.mkdir(self.output_path + 'about/')
        post = MdPost(self.source_path + 'about/index.md')
        post.gen_html()
        self.gen_post_page(post, export_to='about/')

    def move_post_dir(self, post):
        """check is post has a directory, if has, move it to the output_path"""
        posts_source = self.source_path + 'posts/'
        if post.file_root in os.listdir(posts_source):
            shutil.copytree(posts_source + post.file_root,
                            self.output_path + 'posts/' + post.file_root)


    def gen_categories(self):
        self.cat_set = {}
        for post in self.item_list:
            cat = post.meta['categories'][0]
            if cat not in self.cat_set.keys():
                self.cat_set[cat] = []
            self.cat_set[cat].append(post)

        with open(self.output_path + 'category/category.html', 'w') as f:
            for line in self.category_theme.splitlines():
                if re.search(r'{post-categories}', line):
                    cat_line = line
                    continue
                if re.search(r'{post-title}', line):
                    post_line = line
                    for key in self.cat_set.keys():
                            new_line_cat = cat_line.replace(r'{post-categories}',
                            key)
                            f.writelines(new_line_cat)
                            for post in self.cat_set[key]:
                                new_line_post = self.post_link(post_line, post,
                                link_base='../')
                                f.writelines(new_line_post)
                else:
                    f.writelines(line)

pl = PostsList(SOURCE_PATH, OUTPUT_PATH, THEME_PATH)
pl.run()


def s():
    os.chdir(OUTPUT_PATH)
    h = SimpleHTTPRequestHandler
    s = HTTPServer(('', 8000), h)
    print('serving localhost:8000')
    s.serve_forever()
s()

