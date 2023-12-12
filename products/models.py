from django.db import models
import random
import string

def generate_sku():
    """
    Generates a random SKU for the product.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class Category(models.Model):
    """
    Model representing a product category.
    """

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Stock(models.Model):
    """
    Model representing stock information for a product.
    """
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Stock for {self.product.name}"        


class Product(models.Model):
    """
    Model representing a product.
    """
    sku = models.CharField(max_length=254, unique=True, editable=True, default=generate_sku)
    name = models.CharField(max_length=254)
    category_id = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    color = models.CharField(max_length=254, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField()
    image_url = models.URLField(max_length=254, null=True, blank=True)
    image_alt = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=0)
    discount = models.DecimalField(max_digits=8, decimal_places=0, null=True, blank=True)
    favorites = models.ManyToManyField('auth.User', related_name='favorite_products', blank=True)


    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate SKU before saving.
        """
        if not self.sku:
            self.sku = self.generate_sku()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name        