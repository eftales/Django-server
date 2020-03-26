from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import SNSC_data
import json
# Create your views here.


def GetNumfromClassID(request):
    # print('in')
    if request.method == 'GET':
        ClassRoomID = request.GET['classroom_id']
        # print(ClassRoomID)
        BuildingID = request.GET["building_id"]
        if BuildingID[2] == '品':
            louhao = 'P'
        else:
            louhao = 'L'
        BuildingID = louhao + BuildingID[5]
        # print(BuildingID)
        try:
            Num_SQL = SNSC_data.objects.get(
                ClassRoomID=ClassRoomID, BuildingID=BuildingID)
            Num_SQL.BuildingID = Num_SQL.BuildingID[-1]
            result = HttpResponse(json.dumps(
                {"Num": int(Num_SQL.NumofStudent), "resultCode": 200}))
        except:
            result = HttpResponse(json.dumps(
                {"Num": -1, "resultCode": 200}))
        return result

    else:
        return HttpResponse('提交失败')


def ClassNumInit(request, info):
    # print(info)
    try:
        temp = info.split(':')
        BuildingID = temp[0]
        ClassRoomID = temp[1]
        NumofStudent = temp[2]
    except:
        return HttpResponse("info格式不正常，应为：'建筑ID:教室ID:人数'")
    try:
        SNSC_data.objects.create(
            BuildingID=BuildingID, ClassRoomID=ClassRoomID, NumofStudent=NumofStudent)
        return HttpResponse("insert successfully")
    except:
        return HttpResponse("插入异常")


def ClassNumChange(request, info):
    try:
        temp = info.split(':')
        BuildingID = temp[0]
        ClassRoomID = temp[1]
        NumofStudent = temp[2]
    except:
        return HttpResponse("info格式不正常，应为：'建筑ID:教室ID:人数'")
    try:
        data = SNSC_data.objects.get(
            BuildingID=BuildingID, ClassRoomID=ClassRoomID)
        data.NumofStudent = NumofStudent
        data.save()
        return HttpResponse("Change successfully")
    except:
        return HttpResponse("修改异常")


def WelcomePage(request):
    return render_to_response("欢迎界面.html")


def Detail(request, building_id):
    return render_to_response(building_id)
