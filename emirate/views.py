from django.shortcuts import render
from .forms import *


def position_new(request):
    form = PurchaseForm()
    return render(request, 'emirate_purchase.html', {'form': form})
