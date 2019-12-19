# -*- coding: utf-8 -*-
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

if __name__ == '__main__':
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    x = tf.placeholder(tf.float32, [None, 784], name='X')
    y = tf.placeholder(tf.float32, [None, 10], name='Y')
    # 多维的用大写？？
    W = tf.Variable(tf.zeros([784, 10]), name='W')
    b = tf.Variable(tf.zeros([10]), name='b')

    with tf.name_scope("wx_b") as scope:
        y_hat = tf.nn.softmax(tf.matmul(x, W) + b)

    w_h = tf.summary.histogram("weights", W)
    b_h = tf.summary.histogram("biases", b)

    with tf.name_scope('cross-entropy') as scope:
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=y_hat))
        tf.summary.scalar('cross-entropy', loss)
    with tf.name_scope('Train') as scope:
        optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    init = tf.global_variables_initializer()
    merged_summary_op = tf.summary.merge_all()

    with tf.Session() as sess:
        sess.run(init)
        summary_writer = tf.summary.FileWriter('logs', sess.graph)
        max_epochs = 1000
        for i in range(1000):
            batch_xs, batch_ys = mnist.train.next_batch(100)
            _, i, summary_str = sess.run([optimizer, loss, merged_summary_op], feed_dict={x: batch_xs, y: batch_ys})
            summary_writer.add_summary(summary_str, i)

        print('Done')
