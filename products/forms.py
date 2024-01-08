from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances,
    including related products.
    """
    related_products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=CheckboxSelectMultiple,
        required=True,
        label='Related Products - choose at least four items'
    )

    class Meta:
        model = Product
        fields = [
            'sku', 'name', 'category', 'color',
            'size', 'description', 'image', 'image_url',
            'image_alt', 'price', 'discount', 'related_products',
        ]

    image = forms.ImageField(
        label='Image*',
        required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def clean(self):
        """Custom validation for various fields."""
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        discount = cleaned_data.get('discount')
        related_products = cleaned_data.get('related_products')
        image = cleaned_data.get('image')

        if price is not None and price <= 0:
            self.add_error(
                'price',
                forms.ValidationError(
                    "Price should be greater than 0."
                )
            )

        if discount is not None and discount <= 0:
            self.add_error(
                'discount',
                forms.ValidationError(
                    "Discount should be greater than 0."
                )
            )

        if related_products is not None and len(related_products) < 4:
            self.add_error(
                'related_products',
                forms.ValidationError(
                    "Please choose at least four different related products."
                )
            )

        if image is None:
            self.add_error(
                'image',
                forms.ValidationError("Please upload an image.")
            )

        return cleaned_data
