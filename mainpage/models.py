from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Organism(models.Model):
    name=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    creationdate = models.DateTimeField('date published')
    updatedate = models.DateTimeField('date updated')
    organism = models.ForeignKey(Organism, default=1, on_delete=models.SET_DEFAULT)
    text = models.TextField()

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.creationdate:
            self.creationdate = timezone.now()
        if not self.author:
            self.author = request.user
        self.updatedate = timezone.now()
        return super().save(*args, **kwargs)
