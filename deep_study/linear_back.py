import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf


# import

def normalize(x):
    mean = np.mean(x)
    std = np.std(x)
    x = (x - mean) / std
    return x


if __name__ == '__main__':
    boston = tf.contrib.learn.datasets.load_dataset('boston')
    x_train, y_train = boston.data[:, 5], boston.target
    n_samples = len(x_train)

    X = tf.placeholder(tf.float32, name='X')
    Y = tf.placeholder(tf.float32, name='Y')
    b = tf.Variable(0.0)
    w = tf.Variable(0.0)

    Y_hat = X * w + b
    loss = tf.square(Y - Y_hat, name='loss')

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

    init_op = tf.global_variables_initializer()
    total = []

    with tf.Session() as sess:
        sess.run(init_op)
        writer = tf.summary.FileWriter('logs', sess.graph)

        for i in range(100):
            total_loss = 0
            for x, y in zip(x_train, y_train):
                _, this_loss = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
                total_loss += this_loss
            total.append(total_loss / n_samples)
            print('Epoch {0}: Loss {1}'.format(i, total_loss / n_samples))
            writer.close()
            b_value, w_value = sess.run([b, w])

            Y_pred = x_train * w_value + b_value
            print("Done")

        plt.plot(x_train, y_train, 'bo', label='Real Data')
        plt.plot(x_train, Y_pred, 'r', label='Predicted Data')
        plt.legend()
        plt.show()
        plt.plot(total)
        plt.show()
