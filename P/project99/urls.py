"""project99 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from doctor.views import( 
    login_page,home_page,patient_det,list_c)

urlpatterns = [
    path('homepage/',home_page,name='home'),
    path('admin/', admin.site.urls),
    path('',login_page),
    path('det/<str:m>/',patient_det,name='detail'),
    path('clients/',list_c,name='clients')
]
