from zqwblog.generator import WebSite
from zqwblog.util import WebSiteServer
from zqwblog.theme.core import BlogTheme
from blog_config import *


blog_theme = BlogTheme(THEME_PATH+'out/', THEME_PATH+'source/')
wb = WebSite(SOURCE_PATH, OUTPUT_PATH, blog_theme)
wb.get_meta(title=TITLE, author=AUTHOR, cname=CNAME)
wb.run()

server = WebSiteServer(wb)
server.run()
