from django.urls import path
from . import views

urlpatterns = [
    path('get_img/<str:map_num>',views.get_img,name="get_img"),
    path('get_probe_message/<str:MACs>',views.get_probe_message,name="get_probe_message"),
    path('get_location',views.get_location,name="get_location"),
]
