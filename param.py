# -*- coding: utf-8 -*-
import json


class Param(object):
    def __init__(self, **kwargs):
        self.args = kwargs


def _base_req(req):
    print json.dumps(req.__dict__)


def main():
    req = Param(gid=1234)
    _base_req(req)
    pass


if __name__ == '__main__':
    main()
