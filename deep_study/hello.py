import tensorflow as tf

if __name__ == '__main__':
    message = tf.constant('Welcome to the exciting world of Deep Neural Networks!')
    with tf.Session() as sess:
        print(sess.run(message).decode())
