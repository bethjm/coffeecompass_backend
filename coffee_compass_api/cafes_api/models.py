from django.db import models

# Create your models here.
class Shops(models.Model):
    photo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    online_order = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    flavor_notes = models.CharField(max_length=15)

class Comments(models.Model):
    person_name = models.CharField(max_length=100)
    coffee_name = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    beverage_type = models.CharField(max_length=20)
    roaster = models.CharField(max_length=30)
    producer = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    comment = models.CharField(max_length=1000)
    sweet = models.IntegerField()
    acidic = models.IntegerField()
    floral = models.IntegerField()
    citrus = models.IntegerField()
    berry = models.IntegerField()
    chocolate = models.IntegerField()
    caramel = models.IntegerField()
    smoky = models.IntegerField()
    bitter = models.IntegerField()
    clean = models.IntegerField()
    shops = models.ForeignKey(Shops, on_delete=models.CASCADE)