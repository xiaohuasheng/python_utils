#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf

t_a = tf.Variable(0, name='counter')
print(t_a)
init = tf.global_variables_initializer()  # 替换成这样就好
print(t_a)
# 使用 Session
with tf.Session() as sess:
    sess.run(init)
    print(t_a)
