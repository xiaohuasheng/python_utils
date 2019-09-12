# -*- coding: utf-8 -*-
import os
import sys


def file_name(file_dir, task_name):
    os.chdir(file_dir)
    for root, dirs, files in os.walk(file_dir):
        if dirs:
            dirs.sort(reverse=True)
            max_num = int(filter(str.isdigit, dirs[0]))
            max_num = max_num + 1
            dir_name = str(max_num) + task_name
            print dir_name
            os.makedirs(os.path.join(file_dir, dir_name))
            filename = dir_name + ".md"
            file_path = os.path.join(file_dir, dir_name, filename)
            print file_path
            open(file_path, 'a').close()
        break


if __name__ == '__main__':
    argv = sys.argv
    tag_desc = argv[1]
    if not tag_desc:
        print "请输入任务名称"
    # root = os.getcwd()
    file_name(r"E:\task", tag_desc)
