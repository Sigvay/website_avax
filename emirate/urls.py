from django.urls import path
from .views import *


urlpatterns = [
    path('add_position', position_new)
]
