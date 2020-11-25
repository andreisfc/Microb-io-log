from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return render(
        request,
        'mainpage/home.html',
        {
        'title': 'Post #1 sobre C. neoformans',
        'author': 'FCA',
        'organism': 'Cryptococcus neoformans',
        'created': datetime.now(),
        'lastmod': datetime.now(),
        }
    )