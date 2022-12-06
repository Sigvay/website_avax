from django.shortcuts import render, get_object_or_404, HttpResponse

from .exports import export_price
from .models import *
from .support import update_minsksklad, count_down_price


def price(request, slug):
    prices = get_object_or_404(ExportPrice, slug=slug)
    result = export_price(str(prices))
    count_down_price(str(prices))
    return result


def update(request):
    update_minsksklad()
    return HttpResponse('База данных обновлена')
