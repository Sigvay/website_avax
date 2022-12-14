from django.contrib import admin

from orders.models import OrderEmirate


@admin.register(OrderEmirate)
class AdminOrderEmirate(admin.ModelAdmin):
    list_display = ['engine', 'count', 'date_add', 'payment', 'completed']
