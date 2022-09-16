import re


class Extractor:
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


class OrgExtractor(Extractor):
    def __init__(self):
        self.extractors = []
        self.addExtractor(r'#\+TITLE\:(?P<val>.*)', 'title')
        self.addExtractor(r'#\+DATE\:(?P<val>.*)', 'date')
        self.addExtractor(r'#\+CATEGORIES\:(?P<val>.*)', 'categories')
        self.addExtractor(r'#\+TAGS\:(?P<val>.*)', 'tags')
        self.addExtractor(r'#\+HTML\:(?P<val>.*)', 'html')