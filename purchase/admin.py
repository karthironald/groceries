from django.contrib import admin
from .models import Store, Purchase, PurchaseItem

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'created_at', 'updated_at']
    search_fields = ['name', 'location']
    list_filter = ['location']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'purchased_at', 'cost', 'store', 'comments', 'created_at', 'updated_at']
    list_filter = ['purchased_at', 'store']

@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['purchase', 'product', 'quantity', 'unit', 'cost', 'created_at', 'updated_at']
    search_fields = ['product']
    list_filter = ['product']