import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

if __name__ == '__main__':
    mnist = input_data.read_data_sets('MNIST_data', one_hot=True)  # 插入数据

    # name在保存模型时非常有用
    x = tf.placeholder("float", [None, 784], name='x')
    W = tf.Variable(tf.zeros([784, 10]), name='W')
    b = tf.Variable(tf.zeros([10]), name='b')
    y = tf.nn.softmax(tf.matmul(x, W) + b, name='y')  # y预测概率分布

    y_ = tf.placeholder("float", [None, 10])  # y_实际概率分布

    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))  # 交叉熵
    # 梯度下降算法以0.01学习率最小化交叉熵
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    init = tf.initialize_all_variables()  # 初始化变量

    sess = tf.Session()
    sess.run(init)
    saver = tf.train.Saver()

    for i in range(1000):  # 开始训练模型，循环1000次
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    saver.save(sess, './minst_model.ckpt')  # 保存模型
    print("done")
