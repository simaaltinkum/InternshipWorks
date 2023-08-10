from django.db import models
from django.db.models import CharField


class Companies(models.Model):
    company_name= models.CharField(max_length=200, unique= True)
    boss_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)

class Operation(models.Model):
    debt = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    def dif(self):
        return (self.credit - self.debt)
