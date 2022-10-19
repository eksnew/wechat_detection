#from django.conf.urls import url, include 22.10.6 fst：修改为下面
from django.urls import path as url, include
from django.contrib import admin
from django.urls import path
from api import views
import sys
import django
sys.path.extend(['C:\\Users\\Ateng\\Desktop\\wechat_detection-main\\app\\DI\\DI\\DIGG'])
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'DIGG.settings'
django.setup()

urlpatterns = [
    url(r'login/', views.CodeView.as_view()),# 这样这个接口就可以用了
]
