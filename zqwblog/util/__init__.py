import os
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler

def clean_dir(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def start_serve(path):
    os.chdir(path)
    h = SimpleHTTPRequestHandler
    s = HTTPServer(('', 8000), h)
    print('serving localhost:8000')
    s.serve_forever()
