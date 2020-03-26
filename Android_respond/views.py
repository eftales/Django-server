from django.shortcuts import render
from django.core import serializers

# Create your views here.
import json
from django.http import HttpResponse
from .models import class_Android_user
import time
import socket


def Analysis(Appneeds):
    case_num = Appneeds[0:4]
    message = Appneeds[4:len(Appneeds)]
    max_len = len(message)

    s_location = 0
    e_location = 0
    s_message = []
    while e_location < max_len:
        if (message[e_location] == ':'):
            s_message.append(message[s_location + 1:e_location])
            s_location = e_location
        e_location += 1
    s_message.pop(0)
    print('******',s_message)
    s_message.append(message[s_location+1:len(Appneeds)])
    print('******',s_message)
    return [case_num, s_message]


def App_reg_2001(request,message):
    user_exsit = class_Android_user.objects.filter(user_name = message[0])
    print(type(user_exsit),len(user_exsit))
    print(user_exsit)
    if user_exsit.count() >= 1:     #不为0表示有用户占用这个名字，不可以使用该用户名
        response_result = {"result":"user name occupied"}
        print("I am in")
        return json.dumps(response_result, ensure_ascii=False)
    print("I am not in")
    user_ip = ''
    try:
        request.META.has_key('HTTP_X_FORWARDED_FOR')
        user_ip =  request.META['HTTP_X_FORWARDED_FOR']  
    except:  
        user_ip = request.META['REMOTE_ADDR']
    
    try:
        class_Android_user.objects.create(user_name = message[0],user_password = message[1],user_IP = user_ip,user_friends = '',user_groups = '',user_message_cache = '')
        response_result = {"result":"succeed"}
        return json.dumps(response_result, ensure_ascii=False)
    except:
        response_result = {"result":"failed"}
        return json.dumps(response_result, ensure_ascii=False)

def App_sign_in_2002(request,message):
    print('****',message)
    user_sign_message = class_Android_user.objects.filter(user_name = message[0], user_password = message[1])
    print("用户信息及格式",type(user_sign_message),user_sign_message)
    if user_sign_message.count() < 1:
        response_result = {"result":"failed"}
        return json.dumps(response_result, ensure_ascii=False)
    else :
        
        user_sign_message = class_Android_user.objects.get(user_name = message[0], user_password = message[1])
        user_message_cache = str(user_sign_message.user_message_cache)
        user_sign_message.user_message_cache = ''
        user_sign_message.save()
        
        return user_message_cache
        
    

def App_send_friends_2003(request,message):

    from_who = message[0]
    to_whom = message[1]
    time = message[2]
    talk = message[3]

    to_whom_object = class_Android_user.objects.get(user_name = to_whom)
    user_TTL = to_whom_object.user_TTL
    TTL = float(time) - float(user_TTL)
    if TTL > 5:     ###这里根据服务器的情况可能需要改一下
        #history = to_whom_object.user_message_cache
        to_whom_object.user_message_cache += time + '\n' + talk + '\n'
        to_whom_object.save()
        print('缓存成功')
        return json.dumps({"result":"缓存成功"}, ensure_ascii=False)
    else:
        user_ip = to_whom_object.user_IP
        #客户端通用接口1991
        #import socket
        timeout = 5
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        try:
            print(user_ip,'*****',len(user_ip),'*****',type(user_ip))
            s.connect((user_ip, 1991))
            print('成功连接')
            data = bytes(talk,encoding = "utf-8")
            s.send(data)
            print('服务器转发成功')
            s.send(b'exit')
            s.close()
            return json.dumps({"result":"转发成功"}, ensure_ascii=False)
        except:
            to_whom_object.user_message_cache += time + '\n' + 'from' + from_who + '\n' + talk + '\n'
            to_whom_object.save()
            return json.dumps({"result":"转发失败，存入缓存区"}, ensure_ascii=False)


'''
    if len(message)<=2:
        print('********',message)
        to_whom = class_Android_user.objects.get(user_name = message[0])

        user_ip = to_whom.user_IP
        print(type(user_ip))
        response_result = user_ip
        return json.dumps(response_result, ensure_ascii=False)
    else :
        to_whom = class_Android_user.objects.get(user_name = message[1])
        user_message_cache = str(to_whom.user_message_cache)
        user_message_cache += str(message[2]) + '\n' + 'from:' + str(message[0]) +'\n' + str(message[3]) + '\n'
        to_whom.user_message_cache = user_message_cache
        to_whom.save()
        return json.dumps({"result":"缓存成功"}, ensure_ascii=False)
'''     


def App_send_group_2004(request,message):
    pass

def App_get_group_2005(request,message):
    pass

def App_set_group_2006(request,message):
    pass

def App_heart_beat_2007(request,message):
    user_ip = ''
    try:
        request.META.has_key('HTTP_X_FORWARDED_FOR')
        user_ip =  request.META['HTTP_X_FORWARDED_FOR']  
    except:  
        user_ip = request.META['REMOTE_ADDR']
    print(user_ip)
    user_object = class_Android_user.objects.get(user_name = message[0])
    user_object.user_TTL = time.time()
    user_object.user_IP = user_ip
    user_object.save()
    return json.dumps({"result":"确认存活"}, ensure_ascii=False)



def Android_needs_response(request,Appneeds):
    func_dic = {'2001':App_reg_2001,
           '2002':App_sign_in_2002,
           '2003':App_send_friends_2003,
           '2004':App_send_group_2004,
           '2005':App_get_group_2005,
           '2006':App_set_group_2006,
           '2007':App_heart_beat_2007,
           }
    result = Analysis(Appneeds)
    case_num = result[0]
    message = result[1]
    print(result[0],result[1])
    func = func_dic[case_num]   #查询字典用[ ]，不是()
    App_json = func(request,message)
    print(App_json)
    return HttpResponse(App_json,content_type="application/json")
