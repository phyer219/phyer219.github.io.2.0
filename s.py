from http.server import HTTPServer, SimpleHTTPRequestHandler
import markdown
import subprocess
import re
import os
import shutil
import sys
import getopt

posts_source_path = './source/posts/'
templates_path = './source/templates/'
temp_path = './temp/'

public_path = './'              # path where the html file export
posts_public_path = public_path + 'posts/'


def merge_file(post, target):   # todo: there may be some simple function
    with open(target, 'w') as t:
        for line in open(templates_path+'head.html'):
            t.writelines(line)
        for line in open(post):
            t.writelines(line)
        for line in open(templates_path+'end.html'):
            t.writelines(line)


class Post:

    def __init__(self, post_file):
        """
        name: file's or folder's name
        """
        self.post_file = post_file
        (self.path, filename_extension) = os.path.split(post_file)
        self.path += '/'         # todo
        (self.name, self.ext) = os.path.splitext(filename_extension)
        self.have_folder = self.name in os.listdir(posts_source_path)
        info = re.search(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<category>[a-z]*)-(?P<url_title>.*)$', self.name)
        self.year = int(info.group('year'))
        self.month = int(info.group('month'))
        self.day = int(info.group('day'))
        self.category = info.group('category')
        self.url_title = info.group('url_title')

    def gen_md_post(self):
        markdown.markdownFromFile(input=self.post_file,
                                  output=temp_path + 'temp.html',  # todo
                                  encoding='utf-8')
        merge_file(temp_path + 'temp.html',
                   posts_public_path + self.name + '.html')

    def gen_org_post(self):
        cmd1 = "emacs "
        cmd1 += '\'' + self.post_file + '\''  # if contains space, '' is
        # necessary

        cmd1 += " --batch --eval '(org-html-export-to-html)'"
        subprocess.run(cmd1, shell=True)
        shutil.move(self.post_file.replace('.org', '.html'),
                    posts_public_path + self.name + '.html')

    def gen_post(self):
        if self.ext == '.md':
            self.gen_md_post()
        elif self.ext == '.org':
            self.gen_org_post()
        if self.have_folder:
            print('=== copy folder ===', self.path + self.name)
            shutil.copytree(self.path + self.name,
                            posts_public_path + self.name)


def gen_single_post(name_ext):
    """generate one post"""
    post = Post(posts_source_path + name_ext)
    print('--- Generating post ---', post.name)
    post.gen_post()


def gen_index():
    """generate index"""
    posts = []
    for p in os.listdir(posts_public_path):
        if re.search(r'\.html$', p):
            posts.append(Post(posts_source_path + p))
    posts.sort(key=lambda p: (p.year, p.month, p.day), reverse=True)

    with open('index.html', 'w') as t:
        for line in open(templates_path+'index_temp.html'):
            if re.search(r'{path}', line):
                for post in posts:
                    print('--- Generating post ---', post.name)
                    new_line = line.replace(r'{path}',
                                            posts_public_path+post.name+'.html')
                    # todo
                    title = f'{post.year:n}.{post.month:n}.{post.day:n}  '
                    title += post.url_title
                    new_line = new_line.replace(r'{title}', title)
                    t.writelines(new_line)
            else:
                t.writelines(line)


def gen_all():
    """generate all posts, and index"""
    if os.path.exists(posts_public_path):
        shutil.rmtree(posts_public_path)
    os.mkdir(posts_public_path)  # todo
    if not os.path.exists(temp_path):
        os.mkdir(temp_path)
    posts = []
    for name_ext in os.listdir(posts_source_path):
        if re.search(r'\.md$', name_ext) or re.search(r'\.org$', name_ext):
            post = Post(posts_source_path + name_ext)
            posts.append(post)
            gen_single_post(name_ext)

    gen_index()
    shutil.rmtree(temp_path)


def s():
    h = SimpleHTTPRequestHandler
    s = HTTPServer(('', 8000), h)
    print('serving localhost:8000')
    s.serve_forever()


# g_md('./md.md')
# g_org('./lt.org')

opts, args = getopt.getopt(sys.argv[1:], 'asip:')
for opt, v in opts:
    if opt == "-a":
        # generate all posts and index
        gen_all()
    elif opt == "-s":
        # start server
        s()
    elif opt == "-i":
        # generate index
        gen_index()
    elif opt == "-p":
        # generate one post, given filename.extension
        gen_single_post(v)
