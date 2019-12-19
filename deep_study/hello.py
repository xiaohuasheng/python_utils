import tensorflow as tf


def hello():
    message = tf.constant('Welcome to the exciting world of Deep Neural Networks!')

    with tf.Session() as sess:
        print(sess.run(message).decode())


def vector_add():
    v_1 = tf.constant([1, 2, 3, 4])
    v_2 = tf.constant([2, 1, 5, 3])
    v_add = tf.add(v_1, v_2)
    with tf.Session() as sess:
        wirter = tf.summary.FileWriter('logs/', sess.graph)
        print(sess.run(v_add))


def type_list():
    zero_t = tf.zeros([2, 3], tf.int32)
    # 如果在定义部分使用 print 语句，只会得到有关张量类型的信息，而不是它的值
    print(zero_t)
    with tf.Session() as sess:
        print(sess.run(zero_t))


if __name__ == '__main__':
    vector_add()
    # type_list()
    pass
