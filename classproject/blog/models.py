from django.db import models
from django.utils import timezone
#Django Tutorial below
from django.shortcuts import render
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length = 50)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    replies_from_others = models.TextField(default = "none")
    id = models.IntegerField()
    
    def __str__(self):
        return self.title

## Below is from the Django Girls Tutorial
#class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

    # def __str__(self):
    #     return self.title
     
