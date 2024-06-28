from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Choices(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=40, null=True, blank=True,)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='post')
    body=models.CharField(max_length=10000)
    choices=models.ForeignKey(Choices, on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        return reverse("home")