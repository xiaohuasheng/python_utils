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


if __name__ == '__main__':
    # t8t_sys_proxy-c0a8297e-435327-189893
    parse_cmid('t8t_sys_proxy-c0a8297e-435391-192905')
