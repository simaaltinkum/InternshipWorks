from django.db import models

class Email(models.Model):
    email = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    def __str__(self):
        return self.email


