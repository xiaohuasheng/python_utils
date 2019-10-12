# -*- coding: utf-8 -*-
import os
import sys
import time


def get_format_datetime(date_format='%Y-%m-%d'):
    return time.strftime(date_format, time.localtime(time.time()))


def is_weekend():
    which_day = int(time.strftime("%w", time.localtime()))
    if which_day == 6 or which_day == 0:
        return True
    return False


def main():
    argv = sys.argv
    force_gen = False
    try:
        force_gen = argv[1]
    except IndexError as e:
        pass
    if not force_gen and is_weekend():
        print "今天是周末，不生成"
        exit(0)
    filename = get_format_datetime() + ".md"
    file_path = os.path.join('/root/e_drive/dayReflection', filename)
    open(file_path, 'a').close()


if __name__ == "__main__":
    main()
