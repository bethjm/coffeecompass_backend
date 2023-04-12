from rest_framework import serializers 
from .models import Comments
from .models import Shops 

class ShopsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Shops 
        fields = ('id', 'photo', 'name', 'phone','online_order', 'address', 'description','flavor_notes')


class CommentsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comments 
        fields = ('id', 'person_name', 'coffee_name', 'origin','beverage_type', 'roaster', 'producer','price', 'comment', 'sweet','acidic', 'floral', 'citrus','berry', 'chocolate', 'caramel','smoky', 'bitter', 'clean','shops')