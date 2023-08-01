from django.contrib import admin

from .models import Product

class AdminSiteProduct(admin.ModelAdmin):
    list_display = ["name", "short_description", "price"]
    list_filter = ["is_available", "price"]
    search_fields = ["name"]

admin.site.register(Product, AdminSiteProduct)