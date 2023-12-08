from django.contrib import admin
from .models import Product, Category, Stock


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category_id',
        'price',
        'image',
        'get_stock_quantity',
    )

    ordering = ('sku',)

    def get_stock_quantity(self, obj):
        stock = Stock.objects.filter(product=obj).first()

        return stock.quantity if stock else None

    get_stock_quantity.short_description = 'Stock Quantity'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stock, StockAdmin)