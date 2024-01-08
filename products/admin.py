from django.contrib import admin
from .models import Product, Category, RelatedProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RelatedProductAdmin(admin.ModelAdmin):
    list_display = (
        'from_product',
        'to_product',
)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RelatedProduct, RelatedProductAdmin)
