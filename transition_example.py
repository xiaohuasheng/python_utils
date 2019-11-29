# -*- coding: utf-8 -*-
from transitions import Machine


# 定义一个自己的类
class Matter(object):
    def __init__(self):
        self.attitude = None
        self.from_uat = None

    def from_uat_check(self):
        return self.from_uat

    def is_agree(self):
        return self.attitude == 1

    def is_reject(self):
        return self.attitude == 2


# 状态定义
states = ['start', 'leader_approve', 'deploy', 'end']

# 定义状态转移
# The trigger argument defines the name of the new triggering method
transitions = [
    {'trigger': 'approve', 'source': 'start', 'dest': 'leader_approve'},
    {'trigger': 'approve', 'source': 'leader_approve', 'dest': 'deploy',
     'conditions': ['is_agree', 'from_uat_check']},
    {'trigger': 'approve', 'source': 'leader_approve', 'dest': 'end',
     'conditions': ['is_agree'], 'unless': ['from_uat_check']},
]

if __name__ == "__main__":
    # 初始化
    model = Matter()
    machine = Machine(model=model, states=states, transitions=transitions, initial='leader_approve')

    # Test
    print model.state  # solid
    model.attitude = 1
    model.from_uat = False
    model.approve()
    print model.state

    """
    审批前，审批后的处理
    """
