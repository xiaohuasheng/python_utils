# -*- coding: utf-8 -*-
import re

import pinyin


def to_pinyin(var_str):
    return pinyin.get(var_str, format='strip', delimiter="")


def get_yun(word_info_list):
    """
    :param word_info_list:
    word_info = {
        "word": "文",
        "pinyin": "wen"
    }
    :return:
    """
    # word_info_list = [
    #     {
    #         "word": "瓶颈",
    #         "pinyin": "pinjing"
    #     },
    #     {
    #         "word": "并行",
    #         "pinyin": "bingxing"
    #     }
    # ]
    yun_list = [
        "ang", "eng", "ing", "ong", "iang", "uang", "ueng", "iong", "ng",
        "ian", "uan", "van", "uen", "an", "en", "in", "un",
        "iao", "iou", "uai", "uei", "ai", "ei", "ao", "ou", "ia", "ie", "ua", "uo", "ve",
        "a", "o", "e", "i", "u", "v", "er",
    ]
    # yun_list.sort(reverse=True)
    yun_word_map = {}
    for word_info in word_info_list:
        for yun in yun_list:

            re_exp = r'(.*%s$)' % yun
            match_obj = re.match(re_exp, word_info['pinyin'], re.M | re.I)
            if match_obj:
                if yun in yun_word_map:
                    yun_word_map[yun].append(word_info)
                else:
                    yun_word_map[yun] = []
                    yun_word_map[yun].append(word_info)
                break

    return yun_word_map


if __name__ == "__main__":
    # seg_list = jieba.cut("识别核心和重点分析资源瓶颈巧用冗余简化问题多用空间换时间提前准备数据异步和并行")  # 默认是精确模式
    # seg_list = jieba.cut("代码全局初始化静态数据未堆栈")  # 默认是精确模式
    # 代码未全局，堆栈静数据
    # seg_list = jieba.cut("虚箭依,实箭关,虚三接,实三父,空菱聚,实菱组")
    # seg_list = ["虚箭依", "实箭关", "虚三接", "实三父", "空菱聚", "实菱组"]
    """
    虚实三接父
    空实菱聚组
    虚箭是依赖
    实箭关联出
    """
    """
    高性能并发可用(高性并可用)
    估算系统规模和负载
    确定预期技术指标数据
    分析风险因素点
    规划系统结构和数据表
    架构模式框架
    分治瓶颈雪崩墨菲底线思维
    
    缓存异步算法空间换时间冗余降级分布式自动化
    作用特性
    常思常新
    经常预演
    """

    word_info_list = []
    for word in seg_list:
        word_pinyin = to_pinyin(word)
        word_info_list.append(
            {
                "word": word,
                "pinyin": word_pinyin
            }
        )
    yun_word_map = get_yun(word_info_list)
    for yun in yun_word_map:
        print yun
        print ",".join([word_info['word'] for word_info in yun_word_map[yun]])
