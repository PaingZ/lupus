from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='blog/static/blog/image/',blank=True)
    price = models.CharField(max_length=250)
    stock = models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
