#这是我 自己加上的欢迎页面

from django.http import HttpResponse

def index(request):
    print(type(request),request)
    return HttpResponse("Hello,world\n",request)
