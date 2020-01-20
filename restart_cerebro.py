# -*- coding: utf-8 -*-
"""
Check to see if an process is running. If not, restart.
Run this in a cron job
"""
import os


def get_pid(process):
    pid_cmd = "ps -ef | grep \"%s\" | grep -v grep | awk '{print $2}'" % process
    pid = os.popen(pid_cmd).read()
    print pid
    return pid


def start(process):
    print "Starting..."
    new_process = "nohup %s &" % process
    # new_process = "/usr/local/tomcat8/bin/catalina.sh start"
    os.system(new_process)


def stop(process):
    print "Stop..."
    pid = get_pid(process)
    if pid:
        os.system("kill %s" % pid)
        pid = get_pid(process)
        if pid:
            os.system("kill -9 %s" % pid)


def restart(process):
    stop(process)
    start(process)


if __name__ == '__main__':
    #/root/cerebro/bin/cerebro -Dhttp.port=9090 &
    process_name = "/e/go_workspace/demo/bin/main"  # change this to the name of your process
    restart(process_name)
