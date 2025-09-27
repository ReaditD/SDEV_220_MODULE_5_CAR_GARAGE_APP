from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length = 50)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    replies_from_others = models.TextField(default = "none")
    
    def __str__(self):
        return self.title

     
