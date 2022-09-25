import os
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser


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
    url = "localhost:8000"
    webbrowser.open(url, new=0, autoraise=True)
    s.serve_forever()


def load_file(path):
    with open(path, 'r') as f:
        res = f.read()
    return res


def dump_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
