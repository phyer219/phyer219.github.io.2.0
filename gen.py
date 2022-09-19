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
        """
        self.scan_posts()
        self.gen_index()
        self.gen_categories()

    def init_output(self):
        """
        ->
        clean the output_path (now suppose the output_path has already exists)
        ->
        copy the static file in theme to the output path
        ->
        generate the directories where the output file saves.
        """
        clean_dir(self.output_path)
        shutil.copytree(self.theme_path + 'static', self.output_path + 'static')
        os.mkdir(self.output_path + 'posts')
        os.mkdir(self.output_path + 'category')

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
                if file_extension == '.org':
                    self.add_post(file_root, file_extension)
                elif file_extension == '.md':
                    self.add_post(file_root, file_extension)
        self.item_list.sort(key=lambda p: (p.meta['date'][0]), reverse=True)

    
    def add_post(self, file_root, file_extension):

        post_source = self.source_path + 'posts/' + file_root + file_extension
        if file_extension == '.org':
            post = OrgPost(post_source)
            post.gen_html()
            self.gen_org_post_page(post)
        elif file_extension == '.md':
            post = MdPost(post_source)
            post.gen_html()
            self.gen_md_post_page(post)
        self.item_list.append(post)

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
        post_url =  link_base + 'posts/' + post.file_root + '.html'
        link_html = link_theme.replace(r'{post-url}', post_url)
        link_html = link_html.replace(r'{post-title}', post.meta['title'][0])
        date = '.'.join([str(i) for i in self.get_date(post)])
        link_html = link_html.replace(r'{post-date}', str(date))
        return link_html

    def get_date(self, post):
        date = post.meta['date'][0]
        year = int(date[1:5])
        month = int(date[6:8])
        day = int(date[9:11])
        return year, month, day

    def gen_org_post_page(self, post):
        html = self.post_theme.replace(r'{main}', post.html)
        html = html.replace(r'{title}', post.meta['title'][0])
        html = html.replace(r'{post-date}', post.meta['date'][0])
        if 'tags' in post.meta.keys():
            html = html.replace(r'{post-tags}', str(post.meta['tags']))
        html = html.replace(r'{post-category}', str(post.meta['categories'][0]))

        with open(self.output_path + 'posts/' 
                  + post.file_root + '.html', 'w') as f:
            f.write(html)
        self.move_post_dir(post)

    def gen_md_post_page(self, post):
        html = self.post_theme.replace(r'{main}', post.html)
        html = html.replace(r'{title}', post.meta['title'][0])
        html = html.replace(r'{post-date}', post.meta['date'][0])
        if 'tags' in post.meta.keys():
            html = html.replace(r'{post-tags}', str(post.meta['tags']))
        html = html.replace(r'{post-category}', str(post.meta['categories'][0]))

        with open(self.output_path + 'posts/' 
                  + post.file_root + '.html', 'w') as f:
            f.write(html)
        self.move_post_dir(post)

    def move_post_dir(self, post):
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

