from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Profile, Post

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return HttpResponse("게시판 메인 화면")
    ''' User_info = Member.user_name[0]
    context = {'username' : User_info}
    return render(request, "teamfinder/index.html", context)'''

def onboard(request):
    return HttpResponse("온보딩페이지")
    

def login(request):
    return HttpResponse()

def posts_home(request, post_id):
    latest_post_list = Post.objects.order_by(Post.post_id)[:4]
    return (latest_post_list) 

def posts_page(request, post_id):
    current_post_list = Post.objects.order_by(Post.post_id)[:]
    return(current_post_list)

