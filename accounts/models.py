from django.db import models

# Create your models here.
class Product(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True,)

class Price(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField(null=True, blank=True,)

class ResetToken(models.Model):
    pass

