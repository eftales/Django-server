from django.urls import path
from . import views

urlpatterns = [

    # path('MNIST/', views.MNIST),
    path('YOLO_V3_dective/', views.YOLO_V3_dective),
    path('<str:page_name>', views.get_class),


]

