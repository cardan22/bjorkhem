from django.contrib import admin
from .models import Product, Category, RelatedProduct


class RelatedProductInline(admin.TabularInline):
    model = RelatedProduct
    fk_name = 'from_product'
    extra = 1
    verbose_name_plural = 'RELATED PRODUCTS (Preferably select at least four items)'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    fields = (
        'sku', 'name', 'category', 'color',
        'size', 'description', 'image', 'image_url',
        'image_alt', 'price', 'discount',
    )

    filter_horizontal = ('related_products',)

    ordering = ('sku',)

    inlines = [RelatedProductInline]


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
