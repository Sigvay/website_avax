from django.urls import path
from .views import *

urlpatterns = [
    path('export/<slug:slug>', price, name='priceUrl'),
    path('export/avito/<slug:slug>', price_avito, name='priceUrlAvito'),
    path('update/', update),
]