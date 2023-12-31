from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    exclude = ('purchased_quantity',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'discount_total', 'grand_total',
                       'original_bag', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'address1',
              'address2', 'postcode', 'city', 'delivery_cost',
              'order_total', 'discount_total', 'grand_total',
              'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'discount_total',
                    'delivery_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
