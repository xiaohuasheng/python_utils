# -*- coding: utf-8 -*-
import os
import time


def get_format_datetime(date_format='%Y-%m-%d'):
    return time.strftime(date_format, time.localtime(time.time()))


def main():
    filename = get_format_datetime() + ".md"
    file_path = os.path.join('/root/dayReflection', filename)
    open(file_path, 'a').close()


if __name__ == "__main__":
    main()
