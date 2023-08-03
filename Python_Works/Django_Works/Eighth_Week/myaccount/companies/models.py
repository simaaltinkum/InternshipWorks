from django.db import models

class Companies(models.Model):
    company_name = models.CharField(max_length=200, unique= True)
    boss_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)

class Operation(models.Model):
    debt = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)

"""class Customer(models.Model):
    name = models.CharField(max_length=200)
    debt = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)"""

"""company_to_delete = Companies.objects.get(company_name="Meşe Bilişim")
company_to_delete.delete()


customer_to_delete = Customer.objects.get(name="Sima Altınkum")
customer_to_delete.delete()"""

"""Companies.objects.filter(debt__gt=1).delete()

Customer.objects.filter(debt__gt=5).delete()"""
