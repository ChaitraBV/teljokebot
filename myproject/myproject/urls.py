"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django import views
from django.urls import path
from django.contrib import admin
from django.urls import path
from myapp.views import telegram
from myapp.views import telegram, user_calls
urlpatterns = [
    path('', views.home, name='home'),
    path('button_pressed/', views.button_pressed, name='button_pressed'),
    path('user_calls/', views.user_calls, name='user_calls'),
    path('telegram/', telegram, name='telegram'),
    path('user_calls/', user_calls, name='user_calls'),
]


