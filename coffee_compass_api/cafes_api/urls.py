from django.urls import path
from . import views

urlpatterns = [
    path('api/shops', views.ShopsList.as_view(), name='shops_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/shops/<int:pk>', views.ShopsDetail.as_view(), name='shops_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
