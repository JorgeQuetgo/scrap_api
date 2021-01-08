from django.db import models


class Product(models.Model):
    code = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=65)
    brand = models.CharField(max_length=65)
    price = models.DecimalField(max_digits=20, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
