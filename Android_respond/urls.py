from django.urls import path
from . import views

urlpatterns = [
    
    path('<str:Appneeds>',views.Android_needs_response,name="Android_needs_response"),
]
