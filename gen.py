import os
from zqwblog.generator import WebSite
from zqwblog.util import start_serve
from zqwblog.theme.core import PostTheme

SOURCE_PATH = './source/'
THEME_PATH = './themes/bisque/'
OUTPUT_PATH = './docs/'


pt = PostTheme(THEME_PATH+'out/', THEME_PATH+'source/')
pt.run()
pl = WebSite(SOURCE_PATH, OUTPUT_PATH, THEME_PATH+'out/')
pl.run()

start_serve(OUTPUT_PATH)

