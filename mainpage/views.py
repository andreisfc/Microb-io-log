from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import Group, User
from mainpage.models import Post, Organism

def update_posts():
    from random import choice

    p = Post.objects.all()
    l = choice(range(len(p)))

    for i in range(l):
        choice(p).save()

update_posts()

def home(request,pagenum=1,perpage=5):
    posts = Post.objects.order_by('-creationdate')

    return render(
        request,
        'mainpage/home.html',
        {'posts':posts}
    )

def newpost(request):
    return redirect("")

def detailedpost(request, year, month, slug):
    post = Post.objects.get(slug=slug)
    return render(
        request,
        'mainpage/detailedpost.html',
        {'post':post}
    )

def byorganism(request, slug):
    org = Organism.objects.get(slug=slug)
    posts = Post.objects.filter(organism=org).order_by('-creationdate')
    return render(
        request,
        'mainpage/byorganism.html',
        {'posts':posts,'organism':org.name}
    )

def organisms(request):
    orgs = Organism.objects.order_by('name')
    return render(
        request,
        'mainpage/organisms.html',
        {'orglist':orgs}
    )

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            user.groups.add(Group.objects.get(name='regularUser'))
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(
                request,
                "mainpage/register.html",
                {'form':form}
            )

    form = UserCreationForm
    return render(
        request,
        'mainpage/register.html',
        {'form':form}
    )

def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                messages.success(request, f"Welcome, {username}!")
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, f"Invalid information! Please double check username or password!")
        else:
            messages.error(request, f"Invalid information! Please double check username or password!")

    form = AuthenticationForm()
    return render(
        request,
        'mainpage/login.html',
        {'form':form}
    )

def account(request):
    return redirect("admin/")

def logoutpage(request):
    logout(request)
    messages.success(request, f"Logout successful!")
    return redirect("home")