"""
URL configuration for classproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views as blog_views
from carapp import views as car_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin1/',blog_views.index,name="index"),
    path('admin2/',blog_views.c_1,name="c_1"),
    path('admin3/',blog_views.show_post,name="show_post"),
    path('',car_views.car_list,name="car_list")
]

