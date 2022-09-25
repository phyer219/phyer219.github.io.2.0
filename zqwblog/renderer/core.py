import markdown
import os

from .extractor import MdExtractor, OrgExtractor
from .blockparser import OrgBlockParser
from .renderer import HTMLRenderer
from .filter import OrgFilter
from ..util import load_file


class Processor:
    def __init__(self, extractor, filter, parser, renderer):
        self.extractor = extractor
        self.renderer = renderer
        self.filter = filter
        self.parser = parser
        self.temp = []

    def run(self, post):
        # order matters!!!
        self.extractor.run(post)
        self.parser.run(post)
        self.renderer.run(post)
        self.filter.run(post, self.renderer)


class OrgPost:
    def __init__(self, file_path):
        self.ori_str = load_file(file_path)
        self.file_path = file_path
        root_extension = os.path.split(file_path)[-1]
        (self.file_root,
         self.file_extension) = os.path.splitext(root_extension)
        self.meta = {}
        self.html = ''

    def gen_html(self):
        p = Processor(extractor=OrgExtractor(),
                      filter=OrgFilter(),
                      renderer=HTMLRenderer(),
                      parser=OrgBlockParser())
        p.run(self)
        self.html = '\n'.join(b.data for b in self.blocks)


class MdPost:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.ori_str = f.read()
        self.file_path = file_path
        root_extension = os.path.split(file_path)[-1]
        (self.file_root,
         self.file_extension) = os.path.splitext(root_extension)
        self.meta = {}
        self.html = ''

    def gen_html(self):
        p = Processor(extractor=MdExtractor(),
                      filter=OrgFilter(),
                      renderer=HTMLRenderer(),
                      parser=OrgBlockParser())
        p.run(self)
        self.html = markdown.markdown(self.ori_str, extensions=['tables'])
