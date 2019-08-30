# -*- coding: utf-8 -*-
import jieba
import pinyin
import json
import re


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
    seg_list = jieba.cut("识别核心和重点分析资源瓶颈巧用冗余简化问题多用空间换时间提前准备数据异步和并行")  # 默认是精确模式
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
