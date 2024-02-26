from django.urls import path
from .views import *


urlpatterns = [
    path('',Location,name='location'),
    path('search/',searches,name='search'),
    path('advice/',advice_view,name='advice'),
    path('product/',product,name='show_product'),
    path('showdetall_product/<int:product_id>',Showdetall_product,name='Showdetall_product'),
    path('sell_product/',Sell_product,name='sell_product'),
    path('buy_product/',Buy_product,name='buy_product'),
    path('edit/Allproduct/<int:id>/',update,name='edit'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/',cart,name='cart'),
    path('delete/<int:id>/',delete, name="delete"),
]

