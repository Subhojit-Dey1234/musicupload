from django.contrib import admin
from django.urls import path, include
from play import views

urlpatterns = [
    path('',views.MusicListApi,name='home-api'),
]
