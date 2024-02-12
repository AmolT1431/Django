
from django.contrib import admin
from django.urls import path
from Student_Result import views

urlpatterns = [
    path("",views.index,name='home'),
    path("dashbord/",views.dashboard,name='dashbord')
]
