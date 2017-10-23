# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:29:38 2017

@author: caoyujin
"""
# wordusageapp/urls.py
from django.conf.urls import url
from wordusageapp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
