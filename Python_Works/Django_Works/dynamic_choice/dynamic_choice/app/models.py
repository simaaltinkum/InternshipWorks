from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Saved(models.Model):
    selected_datetime = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.selected_datetime:
            self.selected_datetime = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.selected_datetime)
