# coding=utf-8

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

if __name__ == '__main__':
    # 下载MNIST数据集到'MNIST_data'文件夹并解压
    mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

    # 设置权重weights和偏置biases作为优化变量，初始值设为0
    weights = tf.Variable(tf.zeros([784, 10]))
    biases = tf.Variable(tf.zeros([10]))

    # 构建模型
    x = tf.placeholder("float", [None, 784])
    y = tf.nn.softmax(tf.matmul(x, weights) + biases)  # 模型的预测值
    y_real = tf.placeholder("float", [None, 10])  # 真实值

    cross_entropy = -tf.reduce_sum(y_real * tf.log(y))  # 预测值与真实值的交叉熵
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  # 使用梯度下降优化器最小化交叉熵

    # 开始训练
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    merged = tf.summary.merge_all()  # 将图形、训练过程等数据合并在一起
    # E:\python_workspace\utils\deep_study\logs\events.out.tfevents.1576632924.WATSON-ZENG3
    writer = tf.summary.FileWriter('logs/', sess.graph)

    # 每训练100次后评估模型
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.arg_max(y_real, 1))  # 比较预测值和真实值是否一致
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  # 统计预测正确的个数，取均值得到准确率
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_real: mnist.test.labels}))
    loss_avg = 0
    num_of_batch = 100
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(
            num_of_batch)  # 每次随机选取100个数据进行训练，即所谓的“随机梯度下降（Stochastic Gradient Descent，SGD）”
        _, l, summary_str = sess.run([train_step, accuracy, merged], feed_dict={x: batch_xs,
                                                                                y_real: batch_ys})  # 正式执行train_step，用feed_dict的数据取代placeholder
        loss_avg += l
        loss_avg = loss_avg / num_of_batch
        print("Loss{0}".format(loss_avg))

        # result = sess.run(merged, feed_dict={x: batch_xs, y_real: batch_ys})  # 计算需要写入的日志数据
        writer.add_summary(summary_str, i)
