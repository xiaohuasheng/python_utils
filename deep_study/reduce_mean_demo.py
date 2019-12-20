#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

x = np.array([[1., 2., 3.], [4., 5., 6.]])
with tf.Session() as sess:
    mean1 = sess.run(tf.reduce_mean(x))
    mean2 = sess.run(tf.reduce_mean(x, 0))  # 按列
    mean3 = sess.run(tf.reduce_mean(x, 1))  # 按行

    print(mean1)
    print(mean2)
    print(mean3)

"""
降维操作，
input_tensor
axis None，求全部元素平均值，0按列降维，1按行降维

3.5
[2.5 3.5 4.5]
[2. 5.]
mean1=（1+2+3+4+5+6）/ 6
mean2=[(1+4)/2,(2+5)/2,(3+6)/2]
mean3=[(1+2+3)/3,(4+5+6)/3]
"""
