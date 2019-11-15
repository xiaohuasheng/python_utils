# -*- coding: utf-8 -*-
import base64
import random
import string
import time

import pyperclip
import qiniu
from watchdog.events import *
from watchdog.observers import Observer

from config import *


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
            # upload_to_qiniu(event.src_path)

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


def get_filename(filepath):
    dir_name, filename = os.path.split(filepath)
    filename = filename[7:-4]
    return filename


def convert_to_base64(filepath):
    with open(filepath, "rb") as f:
        base64_data = base64.b64encode(f.read())
    filename = get_filename(filepath)
    html_data = '![%s][%s]\n[%s]:data:image/png;base64,%s' % (filename, filename, filename, base64_data)
    # html_data = '<img src="data:image/jpg;base64,%s"/>' % base64_data
    print html_data
    write_to_clipboard(html_data)


# 生成5位随机文件名
def random_name():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))


# 上传至七牛云
def upload_img(fn, sfx='.jpg'):
    key = random_name() + sfx
    q = qiniu.Auth(QINIU_AK, QINIU_SK)
    token = q.upload_token(QINIU_BUCKET, key, 3600)
    ret, info = qiniu.put_file(token, key, fn)
    if ret != None and ret['key'] == key and ret['hash'] == qiniu.etag(fn):
        return QINIU_DOMAIN + key
    else:
        return False


def upload_to_qiniu(filepath):
    # 'C:\\Users\\watson.zeng\\Pictures\\screenshot\\1.png'
    res_url = upload_img(filepath)
    if res_url:
        filename = get_filename(filepath)
        a_str = '![%s](%s)' % (filename, res_url)
        write_to_clipboard(a_str)
    else:
        print 'UPLOAD FAILED'
        exit(0)


def test():
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
