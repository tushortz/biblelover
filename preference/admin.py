from django.contrib import admin
from preference.models import Setting


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['user', 'theme']
    list_filter = ['theme']
    search_fields = ['user']
    ordering = ['-user']

