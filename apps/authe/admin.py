from django.contrib import admin

from .models import User

class AdminSiteUser(admin.ModelAdmin):
    list_display = ["username", "full_name", "email"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    search_fields = ["username", "phone", "email"]

admin.site.register(User, AdminSiteUser)