import tensorflow as tf
from PIL import Image


def imageprepare():
    file_name = './pic/n_0.png'  # 图片路径
    myimage = Image.open(file_name).convert('L')  # 转换成灰度图
    tv = list(myimage.getdata())  # 获取像素值
    # 转换像素范围到[0 1], 0是纯白 1是纯黑
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva


if __name__ == '__main__':
    init = tf.global_variables_initializer()
    saver = tf.train.Saver

    with tf.Session() as sess:
        sess.run(init)
        saver = tf.train.import_meta_graph('minst_model.ckpt.meta')  # 载入模型结构
        saver.restore(sess, 'minst_model.ckpt')  # 载入模型参数

        graph = tf.get_default_graph()  # 计算图
        x = graph.get_tensor_by_name("x:0")  # 从模型中获取张量x
        y = graph.get_tensor_by_name("y:0")  # 从模型中获取张量y

        prediction = tf.argmax(y, 1)
        while True:
            input("请再写")
            result = imageprepare()
            predint = prediction.eval(feed_dict={x: [result]}, session=sess)
            print("我认为是%d" % predint[0])
