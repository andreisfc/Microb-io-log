from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    creationdate = models.DateTimeField()
    updatedate = models.DateTimeField()
    organism = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return(self.text)