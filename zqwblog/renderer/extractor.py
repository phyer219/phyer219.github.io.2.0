import re


class Extractor:
    """
    the method `run`: input a Post, we modify the Post.ori_str and Post.meta

    For example:
    Post.ori_str = "#+TITLE: a title demo
                    * a first level title "
    Post.meta = {}

    ==>

    Post.ori_str = "* a first level title"
    Post.meta = {'title': 'a title demo'}
    """
    def addExtractor(self, pattern, name):
        def extractor(post):
            lines = post.ori_str.split('\n')
            def popi(lines):
                for i, l in enumerate(lines):
                    match = re.search(pattern, l)
                    if match:
                        lines.pop(i)
                        post.meta.setdefault(name, []) # for multiline html tags
                        post.meta[name].append(match.group('val').strip())
                        popi(lines)
            popi(lines)
            post.ori_str = '\n'.join(lines)
            return None
        self.extractors.append(extractor)

    def run(self, post):
        for ex in self.extractors:
            ex(post)
        self.prettify_meta(post)

    def prettify_meta(self, post):
        pass


class OrgExtractor(Extractor):
    def __init__(self):
        self.extractors = []
        self.addExtractor(r'#\+TITLE\:(?P<val>.*)', 'title')
        self.addExtractor(r'#\+DATE\:(?P<val>.*)', 'date')
        self.addExtractor(r'#\+CATEGORIES\:(?P<val>.*)', 'categories')
        self.addExtractor(r'#\+TAGS\:(?P<val>.*)', 'tags')
        self.addExtractor(r'#\+HTML\:(?P<val>.*)', 'html')

class MdExtractor(Extractor):
    def __init__(self):
        self.extractors = []
        self.addExtractor(r'^title\:(?P<val>.*)', 'title')
        self.addExtractor(r'^date\:(?P<val>.*)', 'date')
        self.addExtractor(r'^categories\:(?P<val>.*)', 'categories')
        self.addExtractor(r'^tags\:(?P<val>.*)', 'tags')
    
    def prettify_meta(self, post):
        for k in post.meta.keys():
            if k == 'date':
                date = post.meta[k][0]
                date = date.split(r'/')
                date = '-'.join(date)
                date = date.join(['<', '>'])
                post.meta[k][0] = date