import imp
from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='students')
]
