from django.db import models

# Create your models here.

class Product_Category(models.Model):
    category =  models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=30, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

