from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import class_probe,class_map
from django.core import serializers
import json
import simplejson
import numpy as np
import time
path = 'G:\\uestc\\大创\\WebServer\\server\\Indoor_Guide'
'''
class class_probe(models.Model):

    MAC = models.TextField()
    location = models.TextField()
    vector = models.TextField()
    map_num = models.TextField()
    others = models.TextField()

class class_map(models.Model):

    num = models.TextField()
    J_img = models.TextField() #格式是 images/p_XX.jpg
'''
def get_probe_message(request,MACs):#只有4个MAC
    probe_message = dict()
    n = 1

    for each in MACs:
        print(each,'****',type(each))
        temp = class_probe.objects.get(MAC = each)

        print(temp,'****',type(temp))
        message = dict()
        message['MAC'] = temp.MAC
        message['location'] = temp.location
        message['vector'] = temp.vector
        message['map_num'] = temp.map_num
        message['others'] = temp.others
        probe_message[n] =  message
        n += 1
    print('*******数据封装完成*****')
    for each in probe_message:
        print(each)

    return HttpResponse(JsonResponse(probe_message),content_type = "application/json")


def get_img(request,map_num):
    #temp = class_map.objects.get(num = map_num)
    img_link = img_path + map_num 

    return HttpResponse(open(img_link,"rb").read,content_type="image/jpg")

def get_location(request):
    if request.method == 'POST':

        temp = request.body
        temp = temp.decode('utf-8')
        '''
        Android_data = simplejson.loads(temp)
        print('------',Android_data,type(Android_data))
        '''
        print('你的字符串:',temp)
        '''
        temp = Android_data['vector']
        '''
        t1 = time.clock()
        Android_data_mat = np.asmatrix(temp)
        t2 = time.clock()
        print('创建用户矩阵耗时：',t2-t1)
        #print('用户矩阵创建成功',Android_data_mat)

        mat_path = path + '\\' + 'mat1.txt'
        mat1 = []
        t1 = time.clock()
        with open(mat_path,'r') as f:
            str_data = f.read()
            #print('/*/*/*',str_data,type(str_data))
            mat1 = np.asmatrix(str_data)
        t2 = time.clock()
        print('创建mat1矩阵耗时：',t2-t1)

        mat_path = path + '\\' + 'mat2.txt'
        mat2 = []
        t1 = time.clock()
        with open(mat_path,'r') as f:
            str_data = f.read()
            mat2 = np.asmatrix(str_data)
        mat2 = mat2.T
        t2 = time.clock()
        print('创建mat2矩阵耗时：',t2-t1)
        #print('学习矩阵创建成功',mat1,mat2)
        t1 = time.clock()
        mutip_result1 = np.matmul(Android_data_mat,mat1)
 
        mutip_result = np.matmul(mutip_result1,mat2)
        t2 = time.clock()
        print('矩阵乘法耗时：',t2-t1)
        print('矩阵乘法结果:',mutip_result)
        max_v = np.where(mutip_result == np.max(mutip_result))
        http_result = int(max_v[1])
        print('最大值的下标:',http_result)
        return HttpResponse(http_result) 


