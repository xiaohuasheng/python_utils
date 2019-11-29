# -*- coding: utf-8 -*-


# 类比，定义所有流程节点
from statemachine import StateMachine

flow_node = ["start", "leader_approve", "deploy", "rollback", "check", "end"]

AGREE = 1
NOT_AGREE = 2


def start_transitions(attitude):
    new_state = "leader_approve"
    print "流程开始"
    return new_state, AGREE


# 流程节点处理，这里的审批意见是动态输入的

def leader_approve_transitions(attitude):
    print "上级审批中"
    if attitude == AGREE:
        new_state = "deploy"
    else:
        new_state = "end"
    return new_state, AGREE


def deploy_transitions(attitude):
    print "部署中"
    if attitude == AGREE:
        new_state = "check"
    else:
        new_state = "rollback"
    return new_state, NOT_AGREE


def rollback_transitions(attitude):
    print "正在回滚"
    if attitude == AGREE:
        new_state = "check"
    else:
        new_state = "rollback"
    return new_state, AGREE


def check_transitions(attitude):
    print "产品验收中"
    if attitude == AGREE:
        new_state = "end"
    else:
        new_state = "rollback"
    return new_state, AGREE


def end_transitions(attitude): pass


if __name__ == "__main__":
    m = StateMachine()
    m.add_state("start", start_transitions)  # 添加初始状态
    m.add_state("leader_approve", leader_approve_transitions)
    m.add_state("deploy", deploy_transitions)
    m.add_state("rollback", rollback_transitions)
    m.add_state("check", check_transitions)
    m.add_state("end", None, end_state=1)  # 添加最终状态

    m.set_start("start")  # 设置开始状态
    m.run(AGREE)

"""
在流程发起的时候保存状态机信息，包括节点，结束节点，状态转换函数，入库
当前节点入库
审批的时候，加载状态机信息，运行一次（当前节点, 审批意见），得到新结点入库

处理方法是内存地址，可以多存一个模块路径，运行一次的时候
"""