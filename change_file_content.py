# -*- coding: utf-8 -*-
import os


def append_to_file(filename, content):
    """
    往文件追加内容
    :param filename:
    :param content:
    :return:
    """
    with open(filename, 'a') as f:
        f.write(content)
        f.close()


def change_content(file_dir):
    os.chdir(file_dir)
    for root, dirs, files in os.walk(file_dir):
        if files:
            for a_file in files:
                if os.path.splitext(a_file)[1] == '.java':
                    append_to_file(a_file, "// by watson\n")


if __name__ == '__main__':
    change_content("/root/e_drive/java_workspace/demo-ps-qaz")
