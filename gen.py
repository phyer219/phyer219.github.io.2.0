import os
from zqwblog.generator import WebSite
from zqwblog.util import start_serve

SOURCE_PATH = './source/'
THEME_PATH = './themes/bisque/out/'
OUTPUT_PATH = './docs/'

pl = WebSite(SOURCE_PATH, OUTPUT_PATH, THEME_PATH)
pl.run()

start_serve(OUTPUT_PATH)

