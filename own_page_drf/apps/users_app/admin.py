from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class CustomUserAdmin(BaseUserAdmin):
    list_display = ["email", "is_staff"]
    ordering = ["email"]

admin.site.register(User, CustomUserAdmin)




