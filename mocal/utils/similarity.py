# -*- coding: utf-8 -*-
import time
from collections import Counter
import jieba
from math import sqrt


def cut(text):  # 把文本切分为分词
    return set(jieba.cut(text, cut_all=True))


def cosine_similarity(compare_text, compared_text):
    # 第一步，分词
    words_list1 = cut(text1)  # 分词集合
    words_list2 = cut(text2)  # 分词集合

    # 第二步，列出所有的词
    union = words_list1 | words_list2  # 两分词集合的并集

    # 第三步，计算词频
    c1 = Counter(words_list1)  # 计算分词出现次数
    count1 = dict(c1.most_common())
    c2 = Counter(words_list2)  # 计算分词出现次数
    count2 = dict(c2.most_common())

    # 第四步，写出词频向量，并计算相似度，多维余弦公式
    sum = 0
    sum_z1_2 = 0
    sum_z2_2 = 0
    for u in union:
        z1 = count1.get(u, 0)
        z2 = count2.get(u, 0)
        sum += z1 * z2
        sum_z1_2 += z1 ** 2
        sum_z2_2 += z2 ** 2

    sim_val = sum / (sqrt(sum_z1_2) * sqrt(sum_z2_2))
    return sim_val


if __name__ == '__main__':
    text1 = '阴影部分周长为__$$__cm；面积为__$$__cm²。（π的取值为3.14）'
    text2 = '阴影部分的周长为__$$__cm；面积为__$$__cm²。'
    print time.time()
    print cosine_similarity(text1, text2)
    print time.time()
