from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_filter = ("publication_sign",)
    search_fields = ("name",)
