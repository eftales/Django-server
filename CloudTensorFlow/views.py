from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
import json
from django.http import JsonResponse
# import tensorflow as tf
# import numpy as np
import gc
from .models import SQL_tensorflow_temp_data
import socket
path_MNIST = './CloudTensorFlow/ModelofTensorflow/ModelofMNIST/'
path_CNNMNIST = './CloudTensorFlow/ModelofTensorflow/ModelofCNNMNIST/'

path_YOLO_img0 = './static/images/YOLO_V3/YOLO0.jpg'
path_YOLO_img1 = './static/images/YOLO_V3/YOLO1.jpg'


YOLO_V3_host = '127.0.0.1'
YOLO_V3_port = 1918


def get_class(request, page_name):
    return render_to_response(page_name)

'''
def MNIST_common(temp_buffer):
    tf.reset_default_graph()
    sess = tf.Session()

    # 普通回归
    saver = tf.train.import_meta_graph(
        path_MNIST + 'MNIST.ckpt.meta')
    saver.restore(sess, path_MNIST + 'MNIST.ckpt')
    feed_x = np.ndarray(shape=(1, 784), dtype=np.float32,
                        buffer=temp_buffer)
    x = tf.get_default_graph().get_tensor_by_name(
        'x:0')
    predict = sess.run(tf.get_default_graph().get_tensor_by_name(
        'y:0'), feed_dict={x: feed_x})
    del saver
    del x
    del sess
    gc.collect()
    return predict


def MNIST_CNN(temp_buffer):
    tf.reset_default_graph()
    sess = tf.Session()
    # CNN
    # print('I am in **----****')
    saver = tf.train.import_meta_graph(
        path_CNNMNIST + 'MNISTCNN.ckpt.meta')
    saver.restore(sess, path_CNNMNIST + 'MNISTCNN.ckpt')
    # print('----****-----')
    feed_x_CNN = np.ndarray(shape=(1, 784), dtype=np.float32,
                            buffer=temp_buffer)
    x = tf.get_default_graph().get_tensor_by_name(
        'x-input:0')
    keep_prob = tf.get_default_graph().get_tensor_by_name('keep_prob:0')
    predict = sess.run(tf.get_default_graph().get_tensor_by_name('y_conv:0'), feed_dict={
        x: feed_x_CNN, keep_prob: 0.8})

    del saver
    del x
    del sess
    gc.collect()

    return predict


def MNIST(request):

    if request.method == 'POST':

        temp_str = request.body.decode('utf-8')
        temp_str = temp_str[1:-1]
        temp_multistr = temp_str.split(',')
        temp_intlist = list(map(lambda x: float(x) / 255, temp_multistr))
        temp_buffer = np.array(temp_intlist)
        result1 = MNIST_common(temp_buffer)
        result1 = result1.reshape((10,)).tolist()
        print('--**--', '1')
        result2 = MNIST_CNN(temp_buffer)
        result2 = result2.reshape((10,)).tolist()
        print('--**--', '2')
        # print('--**--', result2)
        results = [result1, result2]

        return JsonResponse({"results": results})

'''
def YOLO_V3_dective(request):
    if request.method == "POST":
        file = request.FILES.get('img')
        with open(path_YOLO_img0, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((YOLO_V3_host, YOLO_V3_port))
        s.sendall('img is done'.encode('utf-8'))
        msg = s.recv(1024)
        msg = s.recv(1024)
        msg = msg.decode('utf-8')
        print(msg)
        s.close()
        result = get_object_or_404(SQL_tensorflow_temp_data, pk=1)
        result.content = msg
        result.save()

    return render_to_response('YOLO_result.html', {'result': result})


