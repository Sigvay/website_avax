from django.urls import path
from .views import *

urlpatterns = [
    path('export/<slug:slug>', price, name='priceurl'),
    path('update/', update),
]