# -*- coding: utf-8 -*-
import commands
import os


def execute_command(command, ignore_error_status=False):
    print command
    status, output = commands.getstatusoutput(command)
    if not ignore_error_status:
        if status:
            raise Exception(output)
    print output
    return status, output


def restart():
    status, pid = execute_command("pgrep main", ignore_error_status=True)
    if pid:
        cmd = "kill %s" % pid
        execute_command(cmd, ignore_error_status=True)
    os.chdir("/root/e_drive/go_workspace/demo/src/main")
    execute_command("go install")
    execute_command("/root/e_drive/go_workspace/demo/bin/main", ignore_error_status=True)


if __name__ == '__main__':
    restart()
