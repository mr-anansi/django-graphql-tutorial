from django.contrib import admin

from cookbook.ingredients.models import Category, Ingredient

# Register your models here.

admin.site.register(Category)
admin.site.register(Ingredient)