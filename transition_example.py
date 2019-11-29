# -*- coding: utf-8 -*-
from transitions import Machine


# 定义一个自己的类
class Matter(object):
    pass


model = Matter()

# 状态定义
states = ['start', 'leader_approve', 'deploy', 'end']

# 定义状态转移
# The trigger argument defines the name of the new triggering method
transitions = [
    {'trigger': 'agree', 'source': 'start', 'dest': 'leader_approve'},
    {'trigger': 'agree', 'source': 'leader_approve', 'dest': 'deploy'},
    {'trigger': 'agree', 'source': 'deploy', 'dest': 'end'},
    {'trigger': 'agree', 'source': 'end', 'dest': 'end'},
    {'trigger': 'reject', 'source': 'start', 'dest': 'leader_approve'},
    {'trigger': 'reject', 'source': 'leader_approve', 'dest': 'end'},
    {'trigger': 'reject', 'source': 'deploy', 'dest': 'end'},
    {'trigger': 'reject', 'source': 'end', 'dest': 'end'},
]

if __name__ == "__main__":
    # 初始化
    machine = Machine(model=model, states=states, transitions=transitions, initial='leader_approve')

    # Test
    print model.state  # solid
    model.agree()
    print model.state
    model.reject()
    print model.state
    model.agree()
    print model.state

    """
    审批前，审批后的处理
    """
