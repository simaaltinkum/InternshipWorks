from django.db import models

class Qr(models.Model):
    qr = models.CharField(max_length = 170)
    type = models.CharField(max_length = 170)
    image = models.ImageField(upload_to='media/')