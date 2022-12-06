from django.contrib import admin
from .models import *


@admin.register(Sellers)
class AdminSallers(admin.ModelAdmin):
    list_display = ['name', 'geoposition', 'phone', 'description']


@admin.register(Container)
class AdminContainer(admin.ModelAdmin):
    list_display = ['country', 'name', 'moving_warehouse', 'loading_cost',
                   'transportation_costs', 'customs_clearance', 'move',
                   'arrived']


@admin.register(PurchasedEngines)
class AdminPurchase(admin.ModelAdmin):
    list_display = ['container', 'number', 'mark', 'model',
                   'year', 'engine_mark', 'engine_number', 'price', 'warehouse']


@admin.register(EnginesInStock)
class AdminEnginesInStock(admin.ModelAdmin):
    list_display = ['mark', 'model', 'year','fuel', 'engine_mark',
                    'transmission', 'price']
