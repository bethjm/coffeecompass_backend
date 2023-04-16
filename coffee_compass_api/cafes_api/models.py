from django.db import models

# Create your models here.
class Shops(models.Model):
    photo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    online_order = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    sweet = models.IntegerField()
    acidic = models.IntegerField()
    floral = models.IntegerField()
    citrus = models.IntegerField()
    berry = models.IntegerField()
    chocolate = models.IntegerField()
    caramel = models.IntegerField()
    smoky = models.IntegerField()
    bitter = models.IntegerField()
    best_type = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)