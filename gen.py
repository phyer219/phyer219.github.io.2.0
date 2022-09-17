from xml.sax.handler import ContentHandler
from xml.sax import parse
from zqwblog.renderer.core import OrgPost, MdPost
import os
import shutil
import re
from http.server import HTTPServer, SimpleHTTPRequestHandler

POSTS_PATH = './source/posts/'
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
    def __init__(self, posts_path, output_path, theme_path):
        self.posts_path = posts_path
        self.output_path = output_path
        self.theme_path = theme_path
        self.load_theme()
        self.init_output()
        self.item_list = []

    def run(self):
        self.scan_posts()
        self.gen_index()
        self.gen_categories()

    def init_output(self):
        clean_dir(self.output_path)
        shutil.copytree(self.theme_path + 'static', self.output_path + 'static')
        os.mkdir(self.output_path + 'posts')
        os.mkdir(self.output_path + 'category')

    def load_theme(self):
        with open(self.theme_path + 'posts/post.html', 'r') as f:
            self.post_theme = f.read()
        with open(self.theme_path + 'index.html', 'r') as f:
            self.index_theme = f.read()
        with open(self.theme_path + 'category/category.html', 'r') as f:
            self.category_theme = f.read()

    def scan_posts(self):
        dir_list = os.listdir(self.posts_path)
        for p in dir_list:
            if os.path.isfile(self.posts_path + p):
                (file_root, file_extension) = os.path.splitext(p)
                if file_extension == '.org':
                    self.add_post(p)
                elif file_extension == '.md':
                    self.add_post(p)
        self.item_list.sort(key=lambda p: (p.meta['date'][0]), reverse=True)

    
    def add_post(self, root_extension):
        (file_root, file_extension) = os.path.splitext(root_extension)
        if file_extension == '.org':
            
            post = OrgPost(self.posts_path + root_extension)
            post.gen_html()
            if 'date' not in post.meta.keys():    # TODO
                post.meta['date'] = ['<2300-01-01>']
            
            self.gen_org_post_page(post)
        elif file_extension == '.md':
            post = MdPost(self.posts_path + root_extension)
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
        html = html.replace(r'{post-tags}', str(post.meta['tags']))
        html = html.replace(r'{post-category}', str(post.meta['categories'][0]))

        with open(self.output_path + 'posts/' 
                  + post.file_root + '.html', 'w') as f:
            f.write(html)
        self.move_post_dir(post)

    def move_post_dir(self, post):
        if post.file_root in os.listdir(self.posts_path):
            shutil.copytree(self.posts_path + post.file_root,
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

pl = PostsList(POSTS_PATH, OUTPUT_PATH, THEME_PATH)
pl.run()


def s():
    os.chdir(OUTPUT_PATH)
    h = SimpleHTTPRequestHandler
    s = HTTPServer(('', 8000), h)
    print('serving localhost:8000')
    s.serve_forever()
s()

