# -*- coding: utf-8 -*-
import os
import time


def get_format_datetime(date_format='%Y-%m-%d'):
    return time.strftime(date_format, time.localtime(time.time()))


def main():
    a = time.localtime()
    weekday = time.strftime("%w", a)
    if int(weekday) in [0, 6]:
        # 周六日不生成
        exit(0)
    filename = get_format_datetime() + ".md"
    file_path = os.path.join('/root/dayReflection', filename)
    open(file_path, 'a').close()


if __name__ == "__main__":
    main()
