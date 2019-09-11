# -*- coding: utf-8 -*-
import os
import time


def get_format_datetime(date_format='%Y%m%d%H%M%S'):
    return time.strftime(date_format, time.localtime(time.time()))


def execute_command(cmd):
    # print cmd
    import os
    a_pipe = os.popen(cmd, 'r')
    a_text = a_pipe.read()
    a_sts = a_pipe.close()
    if a_sts is None: a_sts = 0
    if a_text[-1:] == '\n': a_text = a_text[:-1]
    # print a_sts
    # print a_text
    if a_sts:
        print cmd
        print a_sts
        print a_text
        raise Exception(a_text)
    return a_sts, a_text


def pull_origin(branch):
    execute_command("git pull origin %s" % branch)


def checkout(branch):
    execute_command("git checkout %s" % branch)
    execute_command("git pull origin %s" % branch)


def get_version(version_str):
    version_list = version_str.split(".")
    version_num = "".join(version_list)
    version_num = str(int(version_num) + 1)
    num_list = list(version_num)
    return ".".join(num_list)


def get_last_tag():
    execute_command("git fetch --tag")
    # 有时需要先grep
    return execute_command("git tag | tail -1")


def push_origin(branch):
    execute_command("git push origin %s" % branch)


class Project(object):
    def __init__(self):
        self.project_dir = '/e/python_workspace/boss-cmdb'

    def push_to_master(self, desc):
        branch = 'master'
        now_branch = self.this_branch()
        self.check()
        pull_origin(branch)
        checkout(branch)
        self.merge_code(now_branch, branch)
        self.add_tag(description=desc)
        push_origin(branch)

    def this_branch(self):
        os.chdir(self.project_dir)
        status, branch = execute_command("git symbolic-ref --short -q HEAD")
        return branch

    def is_clean(self):
        os.chdir(self.project_dir)
        status, output = execute_command("git status")
        if output.find("working tree clean") >= 0 or output.find("nothing to commit") >= 0:
            return True
        return False

    def merge_code(self, now_branch, branch):
        # TODO 能执行这两步吗
        checkout(branch)
        execute_command("git merge %s" % now_branch)

    def add_tag(self, description):
        status, last_tag = get_last_tag()
        new_tag = self.generate_new_tag(last_tag)
        execute_command("git tag -a %s -m %s" % (new_tag, description))

    def check(self):
        if not self.is_clean():
            print "分支不干净，请检查"
            exit(0)

    def generate_new_tag(self, last_tag):
        if not last_tag:
            print "最新tag为空，请手动打tag"
            exit(0)
        author = self.get_author()
        if not author:
            print "请设置提交人"
            exit(0)
        # shejiben-7.3.4.4-201908281659-watson
        # utils-1.2.1-201908050927-watson
        tag_list = last_tag.split("-")
        tag_list[1] = get_version(tag_list[1])
        tag_list[2] = get_format_datetime()
        tag_list[3] = author

        new_tag = "-".join(tag_list)
        return new_tag

    def get_author(self):
        os.chdir(self.project_dir)
        status, author = execute_command("git config --global user.name")
        return author


class BossProject(Project):
    def __init__(self):
        super(BossProject, self).__init__()
        self.project_dir = '/e/python_workspace/boss-cmdb'

    def generate_new_tag(self, last_tag):
        pass
        # TODO
        return ""


class UtilsProject(Project):
    def __init__(self):
        super(UtilsProject, self).__init__()
        # self.project_dir = 'E:\php_workspace\utils'
        self.project_dir = '/var/boss/git@repo.we.com/publish/demo-ps-qd'


class PhpUtilsProject(Project):
    def __init__(self):
        super(PhpUtilsProject, self).__init__()
        # self.project_dir = 'E:\php_workspace\utils'
        self.project_dir = '/root/e_drive/php_workspace/utils'


if __name__ == '__main__':
    tag_desc = "test"
    boss_project = UtilsProject()
    boss_project.push_to_master(tag_desc)
    print "********************************"
    print "***********success**************"
    print "********************************"
