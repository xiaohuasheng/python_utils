# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    a_str = "a.js\nb.css"
    cmd = "python receive.py %s" % a_str
    os.system(cmd)
    pass
