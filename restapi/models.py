from django.db import models


class Message(models.Model):
    text = models.TextField()
    username = models.CharField(max_length=128)
    avatar = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
