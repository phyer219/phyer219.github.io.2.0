import os
import shutil
from ..util import clean_dir


def load_module(path, base):
    with open(path, 'r') as f:
        html = f.read()
    html = html.replace('{base}', base)
    return html


class PageTheme():
    base = ''
    name = ''
    path_rel = ''

    def __init__(self, out_root, source_root):
        self.out_root = out_root
        self.source_root = source_root
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


    def get_head(self, head_source='./head/'):
        head_modules = self.load_head_modules()
        html = '\n<head>\n'
        for m in head_modules:
            html += m
        html += '\n</head>\n'
        return html

    def get_body(self, base='./'):
        self.mod_body = load_module(path=self.source_root+'body/'+ self.name +'_body.html', base=self.base)
        html = self.mod_body
        nav = load_module(path=self.source_root+'body/nav.html', base=self.base)
        footer = load_module(path=self.source_root+'body/footer.html', base=self.base)
        header = load_module(path=self.source_root+'body/header.html', base=self.base)
        html = html.replace('{nav}', nav)
        html = html.replace('{footer}', footer)
        html = html.replace('{header}', header)
        html = html.replace('{base}', base)
        return html

    def load_head_modules(self):
        mods = []
        mods.append(load_module(path=self.source_root+'head/mathjax.html', base=self.base))
        mods.append(load_module(path=self.source_root+'head/highlightjs.html', base=self.base))
        mods.append(load_module(path=self.source_root+'head/fonts.html', base=self.base))
        mods.append(load_module(path=self.source_root+'head/meta.html', base=self.base))
        mods.append(load_module(path=self.source_root+'head/style.html', base=self.base))
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
    def run(self):
        clean_dir(self.out_root)
        shutil.copytree(self.source_root+'static', self.out_root+'static')
        self.genPost()
        self.genIndex()
        self.genCate()
        self.genPostList()
        self.genTags()
    def genPost(self):
        pt = PostTheme(out_root=self.out_root, source_root=self.source_root)
        pt.run()
    def genIndex(self):
        id = IndexTheme(out_root=self.out_root, source_root=self.source_root)
        id.run()
    def genCate(self):
        ca = CategoryTheme(out_root=self.out_root, source_root=self.source_root)
        ca.run()
    def genPostList(self):
        pl = PostListTheme(out_root=self.out_root, source_root=self.source_root)
        pl.run()
    def genTags(self):
        tg = TagsTheme(out_root=self.out_root, source_root=self.source_root)
        tg.run()
