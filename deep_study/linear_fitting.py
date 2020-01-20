#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

# Graphic display
plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.show()

import tensorflow as tf

# 取随机数
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
# y = kx + b
y = W * x_data + b

"""
求损失的最小值
最小二乘法
"""
loss = tf.reduce_mean(tf.square(y - y_data))
"""
梯度下降优化器
有这么多数据，怎么最快接近正确结果？
损失函数是抛物线，选一个点，计算出导数，即图形切线，沿着下降方向再选一个点，逼近最小值
"""
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

# 会话，
sess = tf.Session()
sess.run(init)

for step in range(101):
    sess.run(train)
    if step % 20 == 0:
        # 偏置, y = kx + b
        print(step, sess.run(W), sess.run(b))
        print(step, sess.run(loss))

        # Graphic display
        plt.plot(x_data, y_data, 'ro')
        plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
        plt.xlabel('x')
        plt.xlim(-2, 2)
        plt.ylim(0.1, 0.6)
        plt.ylabel('y')
        plt.legend()
        plt.show()
