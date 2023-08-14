from django.db import models
class WebSiteAyarlari(models.Model):
    collapse_text = models.CharField(max_length=50, null= False, blank= False, default=1)

class Items(models.Model):
    nav_item = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item_2 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item_3 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item4 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item5 = models.CharField(max_length=50, null= False, blank= False, default= 1)
    nav_item6 = models.CharField(max_length=50, null= False, blank= False, default= 1)