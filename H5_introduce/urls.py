from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:H5_id>',views.H5_introduce_detail,name="H5_introduce"),
    #欢迎页面
    path('',views.H5_introduce_welcome_page,name="welcome_page"),
    path('func/<int:H5_id>',views.H5_func,name="H5_func"),
    path('H5_reg/',views.H5_reg,name="H5_reg"),
    path('reg_in/',views.reg_in,name="reg_in"),

    
]
