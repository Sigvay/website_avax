from django.contrib import admin
from .models import *


@admin.register(Mark)
class AdminMark(admin.ModelAdmin):
    list_display = ['name_mark']


@admin.register(Model)
class AdminModel(admin.ModelAdmin):
    list_display = ['mark', 'model']


@admin.register(Engines)
class AdminModel(admin.ModelAdmin):
    list_display = ['name', 'fuel', 'volume_engine', 'type_engine']


@admin.register(FuelEngine)
class AdminFuelEngine(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Transmissions)
class AdminTransmissions(admin.ModelAdmin):
    list_display = ['name']
