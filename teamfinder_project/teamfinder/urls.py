from django.contrib import admin
from django.urls import path, include
import os
from teamfinder import views


urlpatterns = [
    path('', views.index, name='index'),    # 첫화면
    path('admin/', admin.site.urls),    # admin 페이지
    path('onboard/', views.onboard, name='onboard'),
    path('post/', views.posts_home, name='post'),        # 게시글 목록
    path('post/<int:pk>', views.posts_page, name="postpage")     # 게시글 상세
]