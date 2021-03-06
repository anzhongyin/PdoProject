"""PdoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from PdoApp import  views
urlpatterns = [
    url(r'^home/', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^LOGIN/', views.LOGIN),
    url(r'^add/', views.add),
    url(r'^nav/', views.nav),
    url(r'^zhuce/', views.zhuce),
    url(r'^regist/', views.regist),
    url(r'^modify/', views.modify),
    url(r'^information/', views.information),
    url(r'^xiugai/', views.xiugai),
    url(r'^index/', views.index),
]
