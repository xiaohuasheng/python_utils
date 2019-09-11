# -*- coding: utf-8 -*-

def check_hu(node_list):
    node_list.sort()
    a_len = len(node_list)
    for i in range(a_len):
        if node_list[i] == node_list[i + 1]:
            j = i + 2
            remain_list = node_list[j:]
            if check_3n(remain_list) or a_len - 2 == 0:
                return True
    return False


def check_3n(remain_list):
    if len(remain_list) == 0:
        return True
    res, remain_list = remove_straight(remain_list)
    if res:
        if check_3n(remain_list):
            return True
    res, remain_list = remove_three_same(remain_list)
    if res:
        if check_3n(remain_list):
            return True
    return False


def remove_straight(remain_list):
    remove_second = False
    remove_third = False
    to_remove = [remain_list[0]]
    for item in remain_list:
        if item > remain_list[0] + 2:
            break
        if remove_second and remove_third:
            break
        if not remove_second and item == remain_list[0] + 1:
            remove_second = True
            to_remove.append(item)
        if not remove_third and item == remain_list[0] + 2:
            remove_third = True
            to_remove.append(item)
    if remove_second and remove_third:
        for node in to_remove:
            remain_list.remove(node)
        return True, remain_list
    return False, []


def remove_three_same(remain_list):
    if len(remain_list) < 3:
        return True, remain_list
    if remain_list[0] == remain_list[2] and remain_list[1] == remain_list[0]:
        return True, remain_list[3:]
    return False, []


if __name__ == "__main__":
    """
    数字 {01 ~ 09} 表示  {1 ~ 9} 筒

　　数字 {11 ~ 19} 表示  {1 ~ 9} 条

　　数字 {21 ~ 29} 表示  {1 ~ 9} 万

　　数字 {31 33 35 37 } 表示 { 东 南 西 北 }

　　数字 {41 43 45} 表示 {中 發 白}
    """
    node_list = [1, 1, 2, 2, 2, 3, 4, 11, 12, 12, 13, 13, 14, 1]
    # node_list = [1, 1, 2, 2, 3, 3, 4, 4]
    # print remove_straight(node_list)
    # print remove_three_same(node_list)
    print check_hu(node_list)
