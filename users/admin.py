from django.contrib import admin
from .models import *


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'date_joined', 'first_name', 'last_name', 'id_telegram')
    list_display_links = ('username', )
    list_filter = ('is_staff', 'exctended_profile')
    search_fields = ('username', )


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = ('date_query', 'user_id', 'query_name', 'available')
    list_display_links = None
    list_filter = ('available',)
    search_fields = ('user_id',)


@admin.register(UserCheckExport)
class UserCheckExportAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'count', 'date_last')