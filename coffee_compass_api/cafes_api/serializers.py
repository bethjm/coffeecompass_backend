from rest_framework import serializers 
from .models import Comments
from .models import Shops 

class ShopsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Shops 
        fields = ('id', 'photo', 'name', 'phone','online_order', 'address', 'description','sweet', 'acidic','floral', 'citrus', 'berry', 'chocolate', 'caramel', 'smoky', 'bitter', 'best_type', 'price')



