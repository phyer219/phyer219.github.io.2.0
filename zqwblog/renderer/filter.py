import re


class Filter:
    def addFilter(self, pattern, name):
        def filter(block, renderer):
            if not block.protect:
                block.data = re.sub(pattern, renderer.sub(name), block.data)
            return None
        self.filters.append(filter)

    def run(self, post, renderer):
        for b in post.blocks:
            for f in self.filters:
                f(b, renderer)


class OrgFilter(Filter):
    def __init__(self):
        self.filters = []
        self.addFilter(r'\=(?!\s)(?P<data>.+?)(?<!\s)\=', 'codeinline')
        self.addFilter(r'\*(?!\s)(?P<data>.+?)(?<!\s)\*', 'em')
        self.addFilter(r'(\[\[)(?P<url>http.*?)(\]\]|\]\[(?P<tag>.*?)\]\])', 'url')
        self.addFilter(r'(\[\[)(file:)(?P<path>.*?\.(png|jpg|gif))(\]\]|\]\[(?P<figalt>.*?)\]\])', 'figure')
        self.addFilter(r'(\[\[)(file:)(?P<path>.*?\.(py|mp4))(\]\]|\]\[(?P<tag>.*?)\]\])', 'file')

