import re
import time


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
    def __init__(self):
        self.extractors = []
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
        super().__init__()
        self.addExtractor(r'#\+TITLE\:(?P<val>.*)', 'title')
        self.addExtractor(r'#\+DATE\:(?P<val>.*)', 'date')
        self.addExtractor(r'#\+CATEGORIES\:(?P<val>.*)', 'categories')
        self.addExtractor(r'#\+TAGS\:(?P<val>.*)', 'tags')
        self.addExtractor(r'#\+HTML\:(?P<val>.*)', 'html')

    def prettify_meta(self, post):
        for k in post.meta.keys():
            if k == 'date':
                post.meta[k] = self.prettify_meta_date(post.meta[k][0])
            if k == 'tags':
                post.meta[k] = self.prettify_meta_tags(post.meta[k][0])
    def prettify_meta_date(self, old_date: str) -> list:
        """
        old_date in form of: "<2000-02-20>"
        return a list of int, for example: [2000, 2, 20]
        """
        year = int(old_date[1:5])
        month = int(old_date[6:8])
        day = int(old_date[9:11])
        return [year, month, day]

    def prettify_meta_tags(self, old_tags: str) -> list:
        """
        'BEC, Tc'
        ==>
        ['BEC', 'Tc']
        """
        tags = old_tags.split(',')
        tags = [tag.strip() for tag in tags]
        return tags


class MdExtractor(Extractor):
    def __init__(self):
        super().__init__()
        self.addExtractor(r'^title\:(?P<val>.*)', 'title')
        self.addExtractor(r'^date\:(?P<val>.*)', 'date')
        self.addExtractor(r'^categories\:(?P<val>.*)', 'categories')
        self.addExtractor(r'^tags\:(?P<val>.*)', 'tags')
    
    def prettify_meta(self, post):
        for k in post.meta.keys():
            if k == 'date':
                post.meta[k] = self.prettify_meta_date(post.meta[k][0])
            if k == 'tags':
                post.meta[k] = self.prettify_meta_tags(post.meta[k][0])
                
    def prettify_meta_date(self, old_date: str) -> list:
        """
        old_date in form of: "2000/02/20"
        return a list of int, for example: [2000, 2, 20]
        """
        date = old_date[:10].split(r'/')# [:10] somte times, md maybe 2000/02/20 20:00 
        date = [int(d) for d in date]
        return date
    
    def prettify_meta_tags(self, old_tags: str) -> list:
        """
        '[物理, 光学]'
        ==>
        ['物理', '光学']
        """
        tags = old_tags.strip('[')
        tags = tags.strip(']')
        tags = tags.split(',')
        tags = [tag.strip() for tag in tags]
        return tags
