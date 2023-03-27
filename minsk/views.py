from django.shortcuts import render, get_object_or_404, HttpResponse

from .exports import export_price, export_avito
from .models import *
from .support import update_minsksklad, count_down_price


def price(request, slug):
    req = get_object_or_404(ExportPrice, slug=slug)
    price = ExportPrice.objects.get(name=str(req))
    result = export_price(str(req))
    count_down_price(price)
    return result


def price_avito(request, slug):
    req = get_object_or_404(ExportPriceAvito, slug=slug)
    price = ExportPriceAvito.objects.get(name=str(req))
    result = export_avito(price)
    count_down_price(price)
    return result


def update(request):
    update_minsksklad()
    return HttpResponse('База данных обновлена')
