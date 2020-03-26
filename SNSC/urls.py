from django.urls import path
from . import views

urlpatterns = [
    path('ClassNumInit/<str:info>', views.ClassNumInit),
    path('GetNumfromClassID/', views.GetNumfromClassID),
    path('welcome', views.WelcomePage),
    path('<str:building_id>', views.Detail),
    path('ClassNumChange/<str:info>', views.ClassNumChange),

]
