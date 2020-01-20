import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

x = tf.placeholder("float")

y = 2 * x

"""
如果不指定maxval，则默认为1，minval如果大于1,则minval和maxval交换，随机数在之间分布
"""
data = tf.random_uniform([2, 3], 1.1)

with tf.Session() as sess:
    x_data = sess.run(data)
    print(x_data)
    print(sess.run(y, feed_dict={x: x_data}))
