from django.shortcuts import render
from django.http import HttpResponse
from mainpage.models import Post

from django.utils import timezone

## FOR TESTING ONLY

def populate_db(numposts=1):
    from django.contrib.auth.models import User
    from lorem import get_paragraph
    from random import choice

    authors = User.objects.all()
    organisms = ["Bacillus anthracis", "Escherichia coli", "Helicobacter pylori"]

    postcount = Post.objects.count()

    for i in range(numposts):
        # postcount = Post.objects.count()
        p = Post(
            title = f"Titulo temporario {postcount+i**i+1}",
            author = choice(authors).username,
            creationdate = timezone.now(),
            updatedate = timezone.now(),
            organism = choice(organisms),
            text = get_paragraph(count=choice(range(5,10)),sep='<br>'),
        )
        p.save()

def clear_db():
    tmp = Post.objects.all()
    for i in tmp:
        i.delete()

# populate_db()
# populate_db(3)
# clear_db()
# FOR TESTING ONLY


def home(request,pagenum=1,perpage=5):
    # pagenum=3
    # posts = Post.objects.order_by('-creationdate')[pagenum+((pagenum-1)*perpage)-1:perpage+(((pagenum-1)*perpage))]
    posts = Post.objects.order_by('-creationdate')
    return render(
        request,
        'mainpage/home.html',
        {'posts':posts}
    )