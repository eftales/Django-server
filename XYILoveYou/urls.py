from django.urls import path
from . import views

urlpatterns = [

    path('<str:pagename>', views.love_page),



]
