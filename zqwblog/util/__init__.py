import os
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
from multiprocessing import Process
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def clean_dir(dir):
    for f in os.listdir(dir):
        path = os.path.join(dir, f)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def load_file(path):
    with open(path, 'r') as f:
        res = f.read()
    return res


def dump_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


class PostChangeHandler(FileSystemEventHandler):
    def __init__(self, website):
        self.website = website

    def on_modified(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            file_root, file_extension = os.path.splitext(file_name)
            if file_extension == '.org' or file_extension == '.md':
                print('------', event.src_path,
                      'are modified!-------------------')
                self.website.render_post(file_root, file_extension)
                print('post has be rerendered, please refresh the page.')


class WebSiteServer:
    def __init__(self, website):
        """website is a class zqwblog.generator.WebSite"""
        self.website = website

    def run(self):
        watchdog_process = Process(target=self.watch_source)
        watchdog_process.start()

        os.chdir(self.website.output_path)
        h = SimpleHTTPRequestHandler
        s = HTTPServer(('', 8000), h)
        print('serving localhost:8000')
        url = "localhost:8000"
        webbrowser.open(url, new=0, autoraise=True)
        server_process = Process(target=s.serve_forever)
        server_process.start()

        watchdog_process.join()
        server_process.join()

    def watch_source(self):
        """
        during the server runing, generate the post when it is modified.
        """
        path = self.website.source_path + 'posts/'
        event_handler = PostChangeHandler(self.website)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()
        try:
            while True:
                observer.join(1)
        finally:
            observer.stop()
            observer.join()
