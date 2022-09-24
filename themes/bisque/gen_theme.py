import os
import shutil


SOURCE_ROOT = './source/'
OUT_ROOT = './out/'


def load_module(path, base):
    with open(path, 'r') as f:
        html = f.read()
    html = html.replace('{base}', base)
    return html


def clean_dir(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


class PageTheme():
    base = ''
    name = ''
    path_rel = ''

    def __init__(self, out_root, source_root):
        self.out_root = out_root
        self.source_root = source_root
        self.check_path()

    def run(self):
        with open(self.path + self.name + '.html', 'w') as f:
            f.write("""<!DOCTYPE html><html class="no-js" lang="zh">\n""")
            f.write(self.get_head())
            f.write(self.get_body())
            f.write("""\n</html>""")

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

clean_dir(OUT_ROOT)
shutil.copytree(SOURCE_ROOT+'static', OUT_ROOT+'static')

pt = PostTheme(out_root=OUT_ROOT, source_root=SOURCE_ROOT)
pt.run()
id = IndexTheme(out_root=OUT_ROOT, source_root=SOURCE_ROOT)
id.run()
ca = CategoryTheme(out_root=OUT_ROOT, source_root=SOURCE_ROOT)
ca.run()
pl = PostListTheme(out_root=OUT_ROOT, source_root=SOURCE_ROOT)
pl.run()
tg = TagsTheme(out_root=OUT_ROOT, source_root=SOURCE_ROOT)
tg.run()
