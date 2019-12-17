# -*- coding: utf-8 -*-
import os
import time

import requests

IP = '192.168.41.105'
CHECK_URL = 'http://%s:8080/cat/r' % IP


def is_accessible(env):
    cookies = {
        'JSESSIONID': '4820CB1B746C27434CCE5EC5B54A0BA6',
        'env': env,
        '_ga': 'GA1.2.1567216388.1567579966',
        'username': 'root',
        'uid': 'wKgB3V3D/tAq/CMYBCHFAg==',
        'csrftoken': 'qNGh7HsXUbKQhDKvn98ET0Hy2om9MHIV',
        'sessionid': 'gv8cxhfbp3r7siut5jnlqape8ozyn6ox',
        'sessionid_boss': 'uqojwssg7t7rtmm25jqo5xgz3e2vpqxu',
    }

    headers = {
        'Host': 'boss.we.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    # 检查是否502了
    try:
        response = requests.get('http://boss.we.com/cat/r', headers=headers, cookies=cookies, verify=False,
                                timeout=(5, 5))
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
        for item in ['test', 'uat', 'idc']:
            if not is_accessible(item):
                print "%s环境的CAT死了" % item
                if item == 'test':
                    remote_restart(IP)
                    print "重启完成"
            else:
                print "%s的活着" % item
        time.sleep(300)
