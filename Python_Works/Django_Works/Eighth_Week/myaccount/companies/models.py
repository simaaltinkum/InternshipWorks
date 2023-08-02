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

"""data = Companies(company_name="Meşe Bilişim", boss_name="Şahin Mersin", debt=1000, credit=500)
data.save()

data2 = Customer(name="Sima Altınkum", debt=100, credit=1200)
data2.save()

data =  Companies.objects.get(pk=1)
data.delete()

data2 = Customer.objects.get(pk=1)
data2.delete()"""