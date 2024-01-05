from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .widgets import CustomClearableFileInput
from .models import Product, Category, RelatedProduct


class ProductForm(forms.ModelForm):
    """ 
    Form for creating and updating Product instances, 
    including related products.
    """
    related_products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=CheckboxSelectMultiple,
        required=False,
        label='Related Products'
    )

    class Meta:
        model = Product
        fields = fields = ['sku', 'name', 'category', 'color',
                           'size', 'description', 'image', 'image_url',
                           'image_alt', 'price', 'discount', 'related_products',
                          ]

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)                    

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

        if price is not None and price < 0:
            self.add_error('price', forms.ValidationError("Price should not be negative."))

        if discount is not None and discount < 0:
            self.add_error('discount', forms.ValidationError("Discount should not be negative."))

        return cleaned_data


class RelatedProductForm(forms.ModelForm):
    """ Form for creating and updating RelatedProduct instances. """

    class Meta:
        model = RelatedProduct
        fields = ['from_product', 'to_product']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        """ Custom validation for various fields. """
        cleaned_data = super().clean()

        return cleaned_data
