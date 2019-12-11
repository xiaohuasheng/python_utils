# -*- coding: utf-8 -*-
import os
import time


def main():
    while True:
        cmd = 'curl -H "Referer: http://boss.we.com/index.html" http://boss.we.com/api/v1/cmdb/is_building/'
        res = os.popen(cmd).read()
        if "True" in res:
            print "还在构建..."
        else:
            print "完成"
            break
        time.sleep(10)


if __name__ == '__main__':
    main()
