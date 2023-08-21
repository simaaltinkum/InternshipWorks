from django.db import models
from django.contrib.flatpages.models import FlatPage
class WebSiteAyarlari(models.Model):
    collapse_text = models.CharField(max_length=50, null= False, blank= False, default=1)

class Items(models.Model):
    nav_item = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item2 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item3 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item4 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item5 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item6 = models.CharField(max_length=50, null= False, blank= False, default= 1)

class Title(models.Model):
    title = models.CharField(max_length=50, null = False, blank=False, default= 1)

class Email(models.Model):
    email = models.CharField(max_length=50, null = False, blank=False, default=1)

class Telephone(models.Model):
    telephone = models.CharField(max_length=50, null=False, blank=False, default=1)

class Services(models.Model):
    service = models.CharField(max_length=50, null=False, blank=False, default=1)
    service2 = models.CharField(max_length=50, null=False, blank=False, default=1)
    service3 = models.CharField(max_length=50, null=False, blank=False, default=1)
    service4 = models.CharField(max_length=50, null=False, blank=False, default=1)
    service5 = models.CharField(max_length=50, null=False, blank=False, default=1)
    service6 = models.CharField(max_length=50, null=False, blank=False, default=1)
    service7 = models.CharField(max_length=50, null=False, blank=False, default=1)
    service8 = models.CharField(max_length=50, null=False, blank=False, default=1)

class Adresses(models.Model):
    adress = models.CharField(max_length=50, null=False, blank=False, default=1)

