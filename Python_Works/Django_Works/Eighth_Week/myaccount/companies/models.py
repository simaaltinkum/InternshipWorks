from django.db import models

class Companies(models.Model):
    company_name = models.CharField(max_length=200)
    boss_name = models.CharField(max_length=200)
    debt = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    debt = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)