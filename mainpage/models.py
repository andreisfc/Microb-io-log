from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    creationdate = models.DateTimeField()
    updatedate = models.DateTimeField()
    organism = models.CharField(max_length=100)
    text = models.TextField()
