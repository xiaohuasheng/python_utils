# -*- coding: utf-8 -*-
class FlowConfig(object):
    STATE = {
        'start': '开始',
        'end': 'end'
    }


class PublishVueConfig(FlowConfig):
    STATE = dict(FlowConfig.STATE, **{
        'end': '结束'
    })


if __name__ == '__main__':
    print PublishVueConfig.STATE
    # print dict(PublishVueConfig.STATE)
