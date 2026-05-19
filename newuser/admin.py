from django.contrib import admin

from newuser.models import Newuser


@admin.register(Newuser)
class NewuserAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
