from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    creationdate = models.DateTimeField()
    updatedate = models.DateTimeField()
    organism = models.CharField(max_length=150)
    text = models.TextField()

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
