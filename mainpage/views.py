from django.shortcuts import render
from django.http import HttpResponse
from mainpage.models import Post

def home(request,pagenum=1,perpage=5):
    # pagenum=3
    # posts = Post.objects.order_by('-creationdate')[pagenum+((pagenum-1)*perpage)-1:perpage+(((pagenum-1)*perpage))]
    posts = Post.objects.order_by('-creationdate')
    return render(
        request,
        'mainpage/home.html',
        {'posts':posts}
    )

def newpost(request):
    return render(
        request,
        'mainpage/newpost.html'
    )

def detailedpost(request, year, month, slug):
    post = Post.objects.get(slug=slug)
    return render(
        request,
        'mainpage/detailedpost.html',
        {'post':post}
    )

def byorganism(request, slug):
    org = slug.capitalize().replace('-',' ')
    posts = Post.objects.all().filter(organism=org).order_by('-creationdate')
    return render(
        request,
        'mainpage/byorganism.html',
        {'posts':posts,'organism':org}
    )

def organisms(request):
    return render(
        request,
        'mainpage/organisms.html'
    )