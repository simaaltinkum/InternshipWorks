from django.db import models
from django.utils import timezone
import datetime

class Qr(models.Model):
    qr = models.CharField(max_length=170)
    type = models.CharField(max_length=170)
    image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)