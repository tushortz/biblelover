from django.contrib import admin
from bible.models import Bible


@admin.register(Bible)
class BibleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'text']
    readonly_fields = ['book', 'chapter', 'verse', 'text', 'category']
    search_fields = ['text']
    list_filter = ['category', 'book']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
