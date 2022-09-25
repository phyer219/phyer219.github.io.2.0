import os
from ..util import clean_dir, load_file

import shutil


def load_module(path: str, page_theme) -> str:
    html = load_file(page_theme.source_root + path)
    html = html.replace('{base}', page_theme.base)
    return html


class PageTheme():
    base = ''
    name = ''
    path_rel = ''

    def __init__(self, blog_theme):
        self.out_root = blog_theme.out_root
        self.source_root = blog_theme.source_root
        self.check_path()

    def run(self):
        """
        a page:
        head
        body
        """
        self.html = ["""<!DOCTYPE html><html class="no-js" lang="zh">\n"""]

        self.html.append(self.get_head())
        self.html.append(self.get_body())

        self.html.append("""\n</html>""")
        self.html = '\n'.join(self.html)
        with open(self.path + self.name + '.html', 'w') as f:
            f.write(self.html)

    def check_path(self):
        self.path = self.out_root + self.path_rel
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def get_head(self):
        head_modules = self.load_head_modules()
        html = '\n<head>\n'
        for m in head_modules:
            html += m
        html += '\n</head>\n'
        return html

    def get_body(self):
        self.mod_body = load_module('body/' + self.name + '_body.html', self)
        html = self.mod_body
        nav = load_module('body/nav.html', self)
        footer = load_module('body/footer.html', self)
        header = load_module('body/header.html', self)
        html = html.replace('{nav}', nav)
        html = html.replace('{footer}', footer)
        html = html.replace('{header}', header)
        return html

    def load_head_modules(self):
        mods = []
        mods.append(load_module('head/mathjax.html', self))
        mods.append(load_module('head/highlightjs.html', self))
        mods.append(load_module('head/fonts.html', self))
        mods.append(load_module('head/meta.html', self))
        mods.append(load_module('head/style.html', self))
        return mods


class PostTheme(PageTheme):
    base = '../'
    name = 'post'
    path_rel = 'posts/'


class IndexTheme(PageTheme):
    base = './'
    name = 'index'
    path_rel = ''


class PostListTheme(PageTheme):
    base = '../'
    name = 'post_list'
    path_rel = 'category/'


class CategoryTheme(PageTheme):
    base = '../'
    name = 'category'
    path_rel = 'category/'


class TagsTheme(PageTheme):
    base = '../'
    name = 'tags'
    path_rel = 'tags/'


class BlogTheme:
    def __init__(self, out_root, source_root):
        self.out_root = out_root
        self.source_root = source_root

    def generate_theme(self):
        clean_dir(self.out_root)
        shutil.copytree(self.source_root+'static', self.out_root+'static')
        self.genPost()
        self.genIndex()
        self.genCate()
        self.genPostList()
        self.genTags()

    def load_theme(self):
        """load the theme files.
        """
        self.post = load_file(self.out_root + 'posts/post.html')
        self.index = load_file(self.out_root + 'index.html')
        self.post_list = load_file(self.out_root + 'category/post_list.html')
        self.category = load_file(self.out_root + 'category/category.html')
        self.tags = load_file(self.out_root + 'tags/tags.html')

    def genPost(self):
        pt = PostTheme(self)
        pt.run()

    def genIndex(self):
        id = IndexTheme(self)
        id.run()

    def genCate(self):
        ca = CategoryTheme(self)
        ca.run()

    def genPostList(self):
        pl = PostListTheme(self)
        pl.run()

    def genTags(self):
        tg = TagsTheme(self)
        tg.run()
