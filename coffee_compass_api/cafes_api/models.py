from django.db import models

# Create your models here.
class Shops(models.Model):
    photo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    online_order = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    sweet = models.IntegerField(null=True)
    acidic = models.IntegerField(null=True)
    floral = models.IntegerField(null=True)
    citrus = models.IntegerField(null=True)
    berry = models.IntegerField(null=True)
    chocolate = models.IntegerField(null=True)
    caramel = models.IntegerField(null=True)
    smoky = models.IntegerField(null=True)
    bitter = models.IntegerField(null=True)
    best_type = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)