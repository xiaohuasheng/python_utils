# -*- coding: utf-8 -*-
import os
import time

import requests

IP = '192.168.41.105'
CHECK_URL = 'http://%s:8080/cat/r' % IP


def is_accessible(url):
    print url
    # 检查是否502了
    try:
        response = requests.get(url, timeout=(5, 5))
    except requests.exceptions.RequestException as e:
        return False
    if not response:
        return False
    if response.status_code != 200:
        return False
    return True


def check_is_running():
    # netstat -pantu | grep 8080 | grep LISTEN | wc -l
    pass


def remote_restart(ip):
    # cmd = "ssh %s python /root/hello.py" % ip
    cmd = "ssh %s python /root/restart_cat.py" % ip
    os.system(cmd)
    pass


if __name__ == '__main__':
    while True:
        process_name = "catalina"  # change this to the name of your process
        if not is_accessible(CHECK_URL):
            print "死了，准备重启"
            remote_restart(IP)
            print "重启完成"
        else:
            print "活着"
        time.sleep(300)
