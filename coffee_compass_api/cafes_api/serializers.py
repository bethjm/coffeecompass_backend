from rest_framework import serializers 
from .models import Shops 

class ShopsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Shops 
        fields = ('id', 'photo', 'name','online_order', 'address', 'description','sweet', 'acidic', 'floral', 'citrus', 'berry', 'chocolate', 'caramel', 'smoky', 'bitter', 'price')
