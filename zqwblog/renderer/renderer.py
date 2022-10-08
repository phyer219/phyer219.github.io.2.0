class Renderer:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method): return method(*args)
        else: print('Warning! No Render Method:', prefix + name)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def run(self, post):
        for b in post.blocks:
            name = b.btype
            self.callback('render_', name, b)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: match.group(0)
            return result
        return substitution

class HTMLRenderer(Renderer):
    def __init__(self):...
    def render_code(self, block):
        before = f'<pre><code class="language-{block.bmeta["lang"].strip():s}">'
        end = '</code></pre>'
        block.data = block.data.replace(r'<', r'&lt;')
        block.data = block.data.replace(r'>', r'&gt;')
        block.data = before + block.data + end
        return None
    def render_quote(self, block):
        before = '<blockquote>'
        end = '</blockquote>'
        block.data = before + block.data + end
        return None
    def render_table(self, block):
        """block.date is 2D list, which save the table content"""
        before = '<table>\n<tr>\n<td>'
        end = '</td>\n</tr>\n</table>'
        content = ["</td>\n<td>".join(row) for row in block.data]
        content = "</td>\n</tr>\n<tr>\n<td>".join(content)
        block.data = before + content + end
        return None
    def render_math(self, block):
        before = '\n$$'
        end = '$$\n'
        block.data = before + block.data + end
        return None
    def render_paragraph(self, block):
        if block.data[:4] == '<li>':
            return None
        before = '<p>'
        end = '</p>'
        block.data = before + block.data + end
        return None
    def render_heading(self, block):
        level = len(block.block_meta['level'].strip()) + 1
        before = f'<h{level:n}>'
        end = f'</h{level:n}>'
        block.data = before + block.data + end
        return None
    def render_list(self, block):
        li = '<ul>\n'
        for l in block.data:
            li += '<li>' + l + '</li>\n'
        li += '</ul>'
        block.data = li
        return None
    def sub_url(self, match):
        res = f"<a href='{match.group('url'):s}'>"
        if match.group('tag'):
            res += f"{match.group('tag'):s}</a>"
        else:
            res += f"{match.group('url'):s}</a>"
        return res
    # def sub_url(self, match):
    #     return f"<a href='{match.group('url'):s}'>{match.group('tag'):s}</a>"
    def sub_figure(self, match):
        res = f"<p><img src='{match.group('path'):s}'"
        if match.group('figalt'):
            res += f" alt='{match.group('figalt'):s}' max-width:100%><p>"
        else:
            res += " alt='figalt' max-width:100%><p>"
        return res
    def sub_file(self, match):
        res = f"<a href='{match.group('path'):s}'>"
        if match.group('tag'):
            res += f"{match.group('tag'):s}</a>"
        else:
            res += f"{match.group('path'):s}</a>"
        return res
    def sub_codeinline(self, match):
        return f"<code>{match.group('data'):s}</code>"
    def sub_em(self, match):
        return f"<em>{match.group('data'):s}</em>"
    def render_line(self, block):
        if block.data != '':
            print("Warning! There is an unblank Block with btype=line:")
            print('=======', block, '========')
            print('not rendered!')
            return None
