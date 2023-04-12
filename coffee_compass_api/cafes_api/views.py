from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CommentsSerializer
from .serializers import ShopsSerializer
from .models import Shops
from .models import Comments

class ShopsList(generics.ListCreateAPIView):
    queryset = Shops.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = ShopsSerializer # tell django what serializer to use

class ShopsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shops.objects.all().order_by('id')
    serializer_class = ShopsSerializer

class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CommentsSerializer # tell django what serializer to use

class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all().order_by('id')
    serializer_class = CommentsSerializer
