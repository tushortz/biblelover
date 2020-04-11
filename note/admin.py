from django.contrib import admin
from note.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'updated_on', 'public']
    list_filter = ['public', 'updated_on', 'created_on']
    search_fields = ['title', 'text']
    ordering = ['-updated_on']
    autocomplete_fields = ['verses']
