from zqwblog.generator import WebSite
from zqwblog.util import start_serve
from zqwblog.theme.core import BlogTheme
from blog_config import *


blog_theme = BlogTheme(THEME_PATH+'out/', THEME_PATH+'source/')
pl = WebSite(SOURCE_PATH, OUTPUT_PATH, blog_theme)
pl.get_meta(title=TITLE, author=AUTHOR, cname=CNAME)
pl.run()

start_serve(OUTPUT_PATH)
