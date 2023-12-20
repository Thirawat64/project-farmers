from django.urls import path
from .views import *


urlpatterns = [
    path('',Location,name='location'),
    path('search/',searches,name='search'),
    path('advice/',advice_view,name='advice'),
    path('product/',product,name='show_product'),
    path('showdetall_product/<int:product_id>',Showdetall_product,name='Showdetall_product'),
    path('sell_product/',Sell_product,name='sell_product'),
    #path('delete/<int:id>/',delete_view,name='delete')
]

