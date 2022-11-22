import os
import shutil
import re
from datetime import datetime

from ..renderer.core import OrgPost, MdPost
from ..util import clean_dir, dump_file
from ..theme.core import BlogTheme


def post_link(link_theme, post, link_base):
    """create a link html

    link_theme = "...{post-url}...{post-title}...{post-date}"
    ==>
    return link_html = "...path...title...xxxx.x.x" (e.g. 2020.1.1)
    """
    post_url = link_base + 'posts/' + post.file_root + '.html'
    link_html = link_theme.replace(r'{post-url}', post_url)
    link_html = link_html.replace(r'{post-title}', post.meta['title'][0])
    date = '.'.join([str(i) for i in post.meta['date']])
    link_html = link_html.replace(r'{post-date}', date)
    return link_html


def gen_post_list_html(post_list, file_theme, out_path, link_base,
                       page_title, post_list_name):
    """generage a html, which contain a post list"""
    line_theme = ''
    for line in file_theme.splitlines():
        if re.search(r'{post-url}', line):
            line_theme = line
    html_line_list = [post_link(line_theme, p, link_base=link_base)
                      for p in post_list]
    html_line_list = '\n'.join(html_line_list)
    res = file_theme.replace(r"{page-title}", page_title)
    res = res.replace(r'{post-list-name}', post_list_name)
    res = res.replace(line_theme, html_line_list)
    dump_file(out_path, res)


def multi_line_replace(theme, keywords: list, data_list: list) -> str:
    """ For example:
        theme = '<h1>{a}: {b}</h1>'
        keywords = ['{a}', '{b}']
        data_list = [['a1', 'b1'],
                     ['a2', 'b2'],
                     ['a3', 'b3']]
    return:
           "
           <h1>{a1}: {b1}</h1>
           <h1>{a2}: {b2}</h1>
           <h1>{a3}: {b3}</h1>
           "
    """
    html_line_theme = ''
    for line in theme.splitlines():
        if re.search(keywords[0], line):
            html_line_theme = line
    data = []
    for d in data_list:
        line = html_line_theme
        for i, keyword in enumerate(keywords):
            line = line.replace(keyword, d[i])
        data.append(line)
    data = '\n'.join(data)
    return theme.replace(html_line_theme, data)


class WebSite:
    def __init__(self, source_path, output_path, theme: BlogTheme):
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
        self.theme = theme
        self.theme.generate_theme()
        self.theme.load_theme()
        self.init_output()
        self.item_list = []

    def get_meta(self, title, author, cname):
        self.title = title
        self.author = author
        self.cname = cname
        dump_file(self.output_path + 'CNAME', self.cname)

    def run(self):
        """
        steps to generate all blog:

        ->
        scan_rencer_posts(): read all post source files, into a list
                             self.item_list
        ->
        gen_index():
        ->
        gen_categories():
        ->
        gen_tags():
        ->
        gen_about():
        """
        self.scan_render_posts()
        self.gen_index()
        self.gen_category_list_page()
        self.gen_category_content_page()
        self.gen_tags_list_page()
        self.gen_tags_content_page()
        self.gen_about()
        self.gen_site_map()

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
        shutil.copytree(self.theme.out_root + 'static',
                        self.output_path + 'static')
        os.mkdir(self.output_path + 'posts')
        os.mkdir(self.output_path + 'categories')
        os.mkdir(self.output_path + 'tags')

    def scan_render_posts(self):
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
                    sd = post.meta['date'][0] * 1e4
                    sd += post.meta['date'][1] * 1e2
                    sd += post.meta['date'][2]
                    post.meta['sort_date'] = sd
                    self.item_list.append(post)
        self.item_list.sort(key=lambda p: (str(p.meta['sort_date'])), reverse=True)

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
        gen_post_list_html(post_list=self.item_list,
                           file_theme=self.theme.index,
                           out_path=self.output_path + 'index.html',
                           link_base='./',
                           page_title='首页|' + self.title,
                           post_list_name="")

    def gen_post_page(self, post, export_to='posts/'):
        """input a Post, using theme to generate a html file"""

        # write main content html
        html = self.theme.post.replace(r'{main}', post.html)

        # write date
        html = html.replace(r'{title}', post.meta['title'][0])
        date = '.'.join([str(i) for i in post.meta['date']])
        html = html.replace(r'{post-date}', date)

        # write tags
        if 'tags' in post.meta:
            data_list = [[t, '../tags/' + t + '.html']
                         for t in post.meta['tags']]
            html = multi_line_replace(html, ['{post-tags}', '{post-tags-url}'],
                                      data_list)

        html = html.replace(r'{post-category}',
                            str(post.meta['categories'][0]))

        # write category
        post_category_url = '../categories/'
        post_category_url += str(post.meta['categories'][0] + '.html')
        html = html.replace(r'{post-category-url}', post_category_url)
        html = html.replace(r"{page-title}", post.meta['title'][0])

        # save html file
        dump_file(self.output_path + export_to + post.file_root + '.html',
                  html)

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
                            self.output_path + 'posts/' + post.file_root,
                            dirs_exist_ok=True)

    def gen_category_list_page(self):
        self.cat_set = {}
        for post in self.item_list:
            cat = post.meta['categories'][0]
            if cat not in self.cat_set:
                self.cat_set[cat] = []
            self.cat_set[cat].append(post)

        keywords = ['{post-categories}', '{category-url}']
        data = [[c, '../categories/' + c + '.html']
                for c in self.cat_set]
        res = self.theme.category.replace(r"{page-title}", '分类|'+self.title)
        res = multi_line_replace(res, keywords, data)
        dump_file(self.output_path + 'categories/index.html', res)

    def gen_category_content_page(self):
        for c in self.cat_set:
            out_file = self.output_path + 'categories/' + c + '.html'
            gen_post_list_html(post_list=self.cat_set[c],
                               file_theme=self.theme.post_list,
                               out_path=out_file,
                               link_base='../',
                               page_title="分类:"+c,
                               post_list_name="分类:"+c)

    def gen_tags_list_page(self):
        self.tag_set = {}
        for post in self.item_list:
            if 'tags' in post.meta:
                for tag in post.meta['tags']:
                    if tag not in self.tag_set:
                        self.tag_set[tag] = []
                    self.tag_set[tag].append(post)

        keywords = ['{post-tags}', '{tag-url}']
        data_list = [[t, '../tags/' + t + '.html'] for t in self.tag_set]
        res = self.theme.tags.replace(r"{page-title}", "标签|"+self.title)
        res = multi_line_replace(res, keywords, data_list)
        dump_file(self.output_path + 'tags/index.html', res)

    def gen_tags_content_page(self):
        for c in self.tag_set:
            out_file = self.output_path + 'tags/' + c + '.html'
            gen_post_list_html(post_list=self.tag_set[c],
                               file_theme=self.theme.post_list,
                               out_path=out_file,
                               link_base='../',
                               page_title="标签:"+c,
                               post_list_name="标签:"+c)

    def gen_site_map(self):
        site_map = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""
        for dirpath, _, filenames in os.walk(self.output_path):
            if filenames:
                for f in filenames:
                    url = os.path.join(dirpath, f)
                    lastmod = datetime.utcfromtimestamp(os.path.getmtime(url))
                    url = url.replace(self.output_path,
                                      'https://'+self.cname+'/')
                    lastmod = lastmod.isoformat() + 'Z'
                    site_map += '\n  <url>\n    <loc>'
                    site_map += url
                    site_map += '</loc>\n    <lastmod>'
                    site_map += lastmod
                    site_map += '</lastmod>\n  </url>\n'
        site_map += '</urlset>'
        dump_file(self.output_path + 'sitemap.xml', site_map)
