# -*- coding: utf-8 -*-


def to_int(hex_num):
    return int(hex_num, 16)


def parse_ip(ip_str):
    # c0a8297e
    ip_arr = list(ip_str)
    item_list = []
    for i in range(0, len(ip_arr), 2):
        item_list.append(ip_arr[i] + ip_arr[i + 1])
    num_list = []
    for item in item_list:
        num_list.append(str(to_int(item)))
    return ".".join(num_list)


def parse_cmid(cmid):
    id_arr = cmid.split("-")
    app = id_arr[0]
    print "app:%s" % app
    ip = id_arr[1]
    print "ip:%s" % parse_ip(ip)
    # timestamp = id_arr[2]
    # serial_num = id_arr[3]


def list_array(a_str):
    # seg_list = jieba.cut(a_str)
    # seg_list = [word for word in seg_list]
    # print seg_list
    # seg_list = ["高", "性", "并", "可"]
    # seg_list = ["性高潮", "并", "可"]
    # seg_list = ["性高潮病", "可", "用"]
    """
高性(高兴)
高并(糕饼)
高可(高科技)
性高(兴高采烈,性高潮)
性并(性病)
可并性高潮
性高潮并(病)
可性高潮并(病)
    """

    """
    分治瓶颈雪崩墨菲底线思维
分墨(粉末)
分底(粉底)
瓶分(评分)
瓶底(平底)
雪瓶(血瓶)
墨底(摸底)
血瓶瓶底有粉末
    """
    seg_list = ["分", "瓶", '雪', '墨', '底']
    str_len = len(seg_list)
    for i in range(str_len):
        for j in range(str_len):
            if i != j:
                print seg_list[i] + seg_list[j]


if __name__ == '__main__':
    # t8t_sys_proxy-c0a8297e-435327-189893
    # parse_cmid('t8t_sys_proxy-c0a8297e-435391-192905')
    list_array('高性并可用')
