from django.contrib import admin
from .models import Entry
from django_markdown.admin import MarkdownModelAdmin


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title", )}
admin.site.register(Entry, EntryAdmin)