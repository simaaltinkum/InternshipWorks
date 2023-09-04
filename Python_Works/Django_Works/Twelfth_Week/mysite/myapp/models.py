from django.db import models
from django.conf import settings

class Tweet(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)