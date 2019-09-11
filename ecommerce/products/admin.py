from django.contrib import admin

from products.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)