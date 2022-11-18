from django.contrib import admin

from .models import Product, Client, Seller, Sell, DayRule, Item

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Seller)
admin.site.register(Sell)
admin.site.register(DayRule)
admin.site.register(Item)
