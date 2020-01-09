# -*- coding: utf-8 -*-

import requests
import json


class WorkWeChatRobot(object):
    # https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=1da1affc-764a-415f-877e-35277981cec7

    KEY_TEST = 'c2c0a037-2aa5-42be-ac9b-06e79ada8e1b'
    KEY_SHEJIBEN = '259cbbab-dea7-4422-9a3d-9eb993383fd4'
    KEY_RENT_SUBSIDY = '1da1affc-764a-415f-877e-35277981cec7'

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
    work = WorkWeChatRobot()
    to_send = "再次提醒一下大家哦 如果有人离职 麻烦主动联系顾燕哦 2020年4月1日还需要大家再提供一次无房证明和政策性住房信息查询单的电子文档 谢谢"
    work.send_message(to_send)
    pass
