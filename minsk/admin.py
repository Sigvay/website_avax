from django.contrib import admin

from users.models import UserCheckExport
from .models import *


@admin.register(WarehouseMinsk)
class WarehouseMinskAdmin(admin.ModelAdmin):
    list_display = (
        'article', 'price', 'input_article', 'mark_auto', 'original_number', 'volume', 'type_engine', 'fuel')


@admin.register(ShipmentMinsk)
class ShipmentMinskAdmin(admin.ModelAdmin):
    list_display = ('tk', 'client', 'track', 'article', 'shipped')
    list_display_links = ('client',)
    list_filter = ('client',)
    search_fields = ('client',)


@admin.register(ExportPrice)
class CountExportAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_url', 'count', 'date_last')
    exclude = ['url', 'count', 'date_last']
    prepopulated_fields = {"slug": ("name",), }


@admin.register(ExportPriceAvito)
class ExportPriceAvitoAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_url', 'count', 'date_last')
    exclude = ['url', 'count', 'date_last']
    prepopulated_fields = {"slug": ("name",), }
    search_fields = ('name',)
