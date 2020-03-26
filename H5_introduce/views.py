from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse
from .models import class_H5_introduce

# Create your views here.


def H5_introduce_detail(request,H5_id):
    m_H5_introduce = get_object_or_404(class_H5_introduce,pk =H5_id)
    context = {}
    context['model_H5_introduce'] = m_H5_introduce
    return render_to_response('H5_introduce.html',context)######################

def H5_introduce_welcome_page(request):
    m_H5_introduce_welcome_page = class_H5_introduce.objects.all()
    context = {}
    context['model_H5_introduce'] = m_H5_introduce_welcome_page
    return render_to_response("welcome_page.html",context)


def H5_func(request,H5_id):
    m_H5_introduce = get_object_or_404(class_H5_introduce,pk =H5_id)
     
    return render_to_response(m_H5_introduce.J_url)
    

def H5_reg(request):
    return render_to_response('H5_reg.html')

def reg_in(request):
    if request.method == 'GET': 
        Introduce = request.GET['Introduce']
        APP_Name = request.GET['APP_Name']
        Html_Name = request.GET['Html_Name']

        H5_exsit = class_H5_introduce.objects.filter(title = APP_Name)

        if H5_exsit.count() > 1:     #不为0表示有用户占用这个名字，不可以使用该用户名
            response_result = "result :" + "user name occupied"

            return HttpResponse(response_result)
    
        try:
            class_H5_introduce.objects.create(title = APP_Name,content = Introduce,J_url = Html_Name)
            
            return render_to_response("upload.html")
        except:
            response_result = "result :" + "failed"
            return HttpResponse(response_result)
    elif request.method == 'POST': 
        New_H5 = request.FILES.get("New_H5")
        print('******',type(New_H5))
        path = "/home/eftales/server/H5_introduce/templates" + New_H5.name

        with open(path,'wb') as f:
            for chunk in New_H5.chunks():
                f.write(chunk)
        return HttpResponse("congratulations!")

        return HttpResponse("文件上传失败")
