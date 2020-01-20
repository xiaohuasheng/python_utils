# -*- coding: utf-8 -*-

import requests
import json
import commands


def to_send():
    status, week = commands.getstatusoutput("date +%W")
    print week
    return int(week) % 2 == 1


class WorkWeChatRobot(object):
    KEY_TEST = 'c2c0a037-2aa5-42be-ac9b-06e79ada8e1b'
    KEY_RENT_SUBSIDY = '406a589e-1c65-401c-89c4-e38e4622e57f'

    SEND_API = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=KEY'

    def send_message(self, message):
        url = self.SEND_API.replace("KEY", self.KEY_RENT_SUBSIDY)
        headers = {
            'Content-Type': 'application/json',
        }

        params = (
        )

        # proxies = {"http": "http://192.168.3.97:3128"}
        proxies = {}

        data = {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }

        response = requests.post(url, headers=headers, params=params,
                                 data=json.dumps(data), proxies=proxies)


if __name__ == '__main__':
    if not to_send():
        print "还没到时间"
        exit(0)
    work = WorkWeChatRobot()
    to_send = "再次提醒一下大家哦 如果有人离职 麻烦主动联系顾燕哦 2020年4月1日还需要大家再提供一次无房证明和政策性住房信息查询单的电子文档 谢谢"
    work.send_message(to_send)
    print "发送了"
