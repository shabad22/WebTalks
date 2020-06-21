from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.TextField(blank=True, null=True)
    Date_posted = models.DateTimeField(default=timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Slug = models.SlugField(max_length = 250, null = True, blank = True) 
    

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Follower(models.Model):
    user = models.ManyToManyField(User)


