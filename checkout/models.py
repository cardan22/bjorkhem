import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=10, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    discount_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """

        # Calculate the total discount
        discount_total = sum((lineitem.product.price - lineitem.product.discount) * lineitem.quantity for lineitem in self.lineitems.all() if lineitem.product.discount is not None)
        
        # Calculate the order total without discounts
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0

        # Calculate delivery cost
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0

        # Calculate grand total including delivery cost and subtract discount
        self.grand_total = self.order_total + self.delivery_cost - discount_total

        self.discount_total = discount_total

        self.save()


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number        


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total, accounting for the product's discount.
        """

        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

        self.order.update_total()

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'