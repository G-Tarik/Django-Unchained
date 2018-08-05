from django.contrib import admin

from .models import Opinion, Category, Item

admin.site.register(Opinion)
admin.site.register(Category)
admin.site.register(Item)
