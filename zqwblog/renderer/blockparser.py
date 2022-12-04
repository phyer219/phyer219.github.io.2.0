from functools import reduce
import re
from copy import deepcopy


class Block:
    protect = False
    bmeta = {}
    def __init__(self, btype, data):
        self.data = data
        self.btype = btype

    def __repr__(self):
        return f'<{self.btype}><{self.data}>'


class BlocksParser:
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    temp.append(b.data)
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                else:
                    temp.append(b.data)
            elif self.start(b):
                inside = True
                temp.append(b.data)
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None


class SignleLineBlocksParser(BlocksParser):
    pattern = ''
    def run(self, post):
        for b in post.blocks:
            if not b.protect:
                match = re.search(self.pattern, b.data)
                if match:
                    b.btype = self.btype
                    b.data = match.group('data')
                    b.block_meta = deepcopy(match.groupdict())


class OrgMathBlocksParser(BlocksParser):
    protect = True
    btype = 'math'
    def start(self, block):
        return re.search(r'\\begin\{align\*?\}', block.data)
    def end(self, block):
        return re.search(r'\\end\{align\*?\}', block.data)


class OrgCodeBlocksParser(BlocksParser):
    protect = True
    btype = 'code'
    def start(self, block):
        return re.search(r'#\+begin_src(?P<lang>.*?$)', block.data,
                         re.IGNORECASE)
    def end(self, block):
        return re.search(r'#\+end_src', block.data,
                         re.IGNORECASE)
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    #temp.append(b.data)
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.bmeta = bmeta
                    nb.protect = self.protect
                    news.append(nb)
                else:
                    temp.append(b.data)
            elif self.start(b):
                inside = True
                bmeta = {'lang': self.start(b).group('lang')}
                #temp.append(b.data)
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None
class OrgQuoteBlocksParser(BlocksParser):
    protect = True
    btype = 'quote'
    def start(self, block):
        return re.search(r'#\+begin_quote', block.data, re.IGNORECASE)
    def end(self, block):
        return re.search(r'#\+end_quote', block.data, re.IGNORECASE)
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                else:
                    temp.append(b.data)
            elif self.start(b):
                inside = True
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None

class OrgTableBlocksParser(BlocksParser):
    protect = True
    btype = 'table'
    def start(self, block):
        return re.search(r'^(\s*\|)', block.data)
    def end(self, block):
        return re.search(r'^(?!\s*\|)', block.data)
    def run(self, post):
        inside = False
        temp = []
        news = []
        for b in post.blocks:
            if inside:
                if self.end(b):
                    inside = False
                    data = temp
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(b)
                    news.append(nb)
                else:
                    temp.append(b.data.split(r'|'))
            elif self.start(b):
                inside = True
                temp.append(b.data.split(r'|'))
            else:
                news.append(b)
        post.blocks = news
        news = []
        return None

class OrgParagraphBlocksParser(BlocksParser):
    protect = False
    btype = 'paragraph'
    def run(self, post):
        blank = False
        inside = False
        temp = []
        news = []
        for i, b in enumerate(post.blocks):
            if blank and (b.data != '' and b.btype == 'line'):
                # last line blank, this line not blank,
                # that is a start of paragraph!
                inside = True
                temp.append(b.data)
            elif inside:
                if (b.data == '' or b.btype != 'line' 
                    or (i+1)==len(post.blocks)):
                    # inside the paragraph, and this line blank or not a line,
                    # this line should not a paragraph, end it!
                    inside = False
                    data = '\n'.join(temp)
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                    news.append(b)
                else: temp.append(b.data)
            else:
                news.append(b)
            if b.data == '' or b.btype != 'line':
                blank = True
            else:
                blank = False
        post.blocks = news
        news = []
        return None

class OrgListBlocksParser(BlocksParser):
    protect = False
    btype = 'list'
    def run(self, post):
        blank = False
        inside = False
        temp = []
        news = []
        for i, b in enumerate(post.blocks):
            if (b.data[:2] == r'- ' and b.btype == 'line') and not inside:
                inside = True
                temp.append(b.data)
            elif inside:
                if ((blank and b.data != '' and b.data[:2] !='- ') or b.btype != 'line' 
                     or (i+1)==len(post.blocks)):
                    inside = False

                    data = []
                    for ele in temp:
                        if ele[:2] == '- ':
                            data.append(ele[2:].strip())
                        elif ele != '':
                            data[-1] += ' ' + ele.strip()

                    #data = [li.strip() for li in temp if li !='']
                    #'\n'.join(temp) return a list of str
                    temp = []
                    nb = Block(self.btype, data)
                    nb.protect = self.protect
                    news.append(nb)
                    news.append(b)
                elif b.data != '':
                    temp.append(b.data)

            else:
                news.append(b)
            if b.data == '':
                blank = True
            else:
                blank = False
        post.blocks = news
        news = []
        return None


class OrgHeadingBlocksParser(SignleLineBlocksParser):
    btype = 'heading'
    pattern = r'(^|\s)(?P<level>\*+\s)(?P<data>.*)($|\n)'


class OrgBlockParser:
    def __init__(self):
        self._init_blocksparser()

    def _init_blocksparser(self):
        # order matters! TODO: add a prority!
        self.blocksparsers = []
        self.blocksparsers.append(OrgMathBlocksParser())
        self.blocksparsers.append(OrgCodeBlocksParser())
        self.blocksparsers.append(OrgQuoteBlocksParser())
        self.blocksparsers.append(OrgTableBlocksParser())
        self.blocksparsers.append(OrgHeadingBlocksParser())
        self.blocksparsers.append(OrgListBlocksParser())
        self.blocksparsers.append(OrgParagraphBlocksParser())

    def run(self, post):
        lines = post.ori_str.split('\n')
        post.blocks = [Block('line', l) for l in lines]
        for b in self.blocksparsers:
            b.run(post)
