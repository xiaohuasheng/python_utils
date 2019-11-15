# -*- coding: utf-8 -*-
import base64
import time

import pyperclip
from watchdog.events import *
from watchdog.observers import Observer


def write_to_clipboard(a_str):
    pyperclip.copy(a_str)
    # r = tk.Tk()
    # r.withdraw()
    # r.clipboard_clear()
    # r.clipboard_append(a_str)
    # c = r.clipboard_get()
    # print "剪切板：%s" % c.encode("utf8")
    # r.destroy()


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.global_path = ""

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            time.sleep(1)
            if event.src_path == self.global_path:
                print "已经生成了"
                return
            self.global_path = event.src_path
            print event.src_path
            convert_to_base64(event.src_path)

    # def on_moved(self, event):
    #     if event.is_directory:
    #         print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
    #     else:
    #         print event.src_path
    #
    # def on_deleted(self, event):
    #     if event.is_directory:
    #         print("directory deleted:{0}".format(event.src_path))
    #     else:
    #         print event.src_path
    #
    # def on_modified(self, event):
    #     if event.is_directory:
    #         print("directory modified:{0}".format(event.src_path))
    #     else:
    #         print event.src_path
    #


def convert_to_base64(filepath):
    dir_name, filename = os.path.split(filepath)
    with open(filepath, "rb") as f:
        base64_data = base64.b64encode(f.read())
    filename = filename[7:-4]
    html_data = '![%s][%s]\n[%s]:data:image/png;base64,%s' % (filename, filename, filename, base64_data)
    # html_data = '<img src="data:image/jpg;base64,%s"/>' % base64_data
    print html_data
    write_to_clipboard(html_data)


def test():
    # filename = "C:\\Users\\watson.zeng\\Pictures\\screenshot\\screen.png"
    filename = u"C:\\Users\\watson.zeng\\Pictures\\screenshot\\企业微信截图_20191115135954.png"
    convert_to_base64(filename)
    exit(0)


if __name__ == "__main__":
    # test()
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "C:\Users\watson.zeng\Pictures\screenshot", True)
    observer.start()
    print "开始监听"
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
