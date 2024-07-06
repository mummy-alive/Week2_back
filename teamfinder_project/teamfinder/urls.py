from django.contrib import admin
from django.urls import path, include
import os
import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('onboard/', views.onboard, name='onboard')
]