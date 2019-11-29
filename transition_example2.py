# -*- coding: utf-8 -*-
import random

from transitions import Machine


class Matter(object):
    heat = False
    attempts = 0

    def count_attempts(self): self.attempts += 1

    def is_really_hot(self): return self.heat

    def is_really_hot2(self):
        print 'is_really_hot2'
        return False

    def heat_up(self): self.heat = random.random() < 0.25

    def stats(self): print('It took you %i attempts to melt the lump!' % self.attempts)

    def stats2(self): print('It took you %i attempts to melt the lump!' % self.attempts)


states = ['solid', 'liquid', 'gas', 'plasma']

transitions = [
    {'trigger': 'melt', 'source': 'solid', 'dest': 'liquid', 'prepare': ['heat_up', 'count_attempts'],
     'conditions': ['is_really_hot', 'is_really_hot2'], 'after': ['stats', 'stats2']},
]

if __name__ == "__main__":
    lump = Matter()
    machine = Machine(lump, states, transitions=transitions, initial='solid')
    lump.melt()
    lump.melt()
    lump.melt()
    lump.melt()
    lump.melt()

"""
这个例子有定义审批的地方，也有审批后的方法定义，
数据可以固化到表里，审批的时候再取出来初始化
这里的条件就是审批意见和上一个节点是什么，每个节点配置不同的条件
上一个节点，当前节点，
"""
