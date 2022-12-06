from django.contrib import admin

from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('sum', 'article', 'information', 'username', 'date_add')
    search_fields = ('article', )
