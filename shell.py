# -*- coding: utf-8 -*-
import json

import requests


def execute_cmd(cmd):
    cookies = {
        '_ga': 'GA1.2.1567216388.1567579966',
        'username': 'root',
        'uid': 'wKgB3V3D/tAq/CMYBCHFAg==',
        'env': 'uat',
        'csrftoken': 'vKHSZOYTQRwWIncFXV38LOLgQ7D4xwoK',
        'sessionid_boss': '7ib1cci38c0ajrumfo4hkv3fvrcq5bec',
    }

    headers = {
        'Host': 'boss.we.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Origin': 'http://boss.we.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Referer': 'http://boss.we.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        "cmd": cmd
    }
    response = requests.post('http://boss.we.com/api/v1/cmdb/shell/', headers=headers, cookies=cookies, verify=False,
                             data=json.dumps(data))
    if response.status_code != 200:
        exit("auth error")
    return response.json()


if __name__ == "__main__":
    while True:
        cmd = raw_input()
        if not cmd:
            continue
        print execute_cmd(cmd)["output"]
