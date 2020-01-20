# -*- coding: utf-8 -*-
import commands


def execute_command(command, ignore_error_status=False):
    print command
    status, output = commands.getstatusoutput(command)
    if not ignore_error_status:
        if status:
            raise Exception(output)
    print output
    return status, output


if __name__ == '__main__':
    pass
