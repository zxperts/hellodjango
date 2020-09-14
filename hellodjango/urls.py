"""hellodjango URL Configuration

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
from django.urls import path, include
from appone import views
from apptwo import views as apptwo_views
from peoplebook import views as peoplebook_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('djangorocks/', apptwo_views.djangorocks),
    #path('users/', peoplebook_views.users),
    path('peoplebook/', include('peoplebook.urls')),
    path('devices/add/<str:os>/<str:model>/',views.device_add),
    path('devices/<int:id>/', views.device_detail),
    path('devices/filter/<str:os>/', views.devices_filter),
    path('getformdata/', views.get_form_data, name='get-form-data'),
    path('thanks/', views.thanks, name='thanks'),
    path('thanks_user/<str:name>/', views.thanks_user, name='thanks_user'),
    path('register/', views.user_register, name='user-registration')
]
