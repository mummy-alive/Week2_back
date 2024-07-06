from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Profile, Post

def index(request):
    return HttpResponse("시작페이지")

def onboard(request):
    return HttpResponse("온보딩페이지")
    
def login(request):
    return HttpResponse()

def posts_home(request):
    postlist = Post.objects.all()
    return render(request, 'teamfinder/index.html', { 'postlist': postlist })

def posts_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'teamfinder/posting.html', {'post': post})
