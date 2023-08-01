from django.contrib import admin

from .models import Product

#Регистрируем модель Product в админ панели

class AdminSiteProduct(admin.ModelAdmin):
    list_display = ["name", "short_description", "price"] #Отображаемые поля
    list_filter = ["is_available", "price"] #Поля, по которым идёт фильтрация
    search_fields = ["name"] #Поле, по которому идёт поиск

admin.site.register(Product, AdminSiteProduct) #Регистрация в админ панели