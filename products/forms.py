from django import forms
from .models import Product, Category, Stock


class ProductForm(forms.ModelForm):
    """ 
    Form for creating and updating Product instances, 
    including stock information.
    """

    class Meta:
        model = Product
        fields = fields = ['sku', 'name', 'category', 'color',
                           'size', 'description', 'image',
                           'image_alt', 'price', 'discount', 'quantity'
                          ]

    # Add quantity field for stock information
    quantity = forms.IntegerField(label='Quantity in Stock', required=True)    

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
        quantity = cleaned_data.get('quantity')
        price = cleaned_data.get('price')
        discount = cleaned_data.get('discount')

        if quantity is not None and quantity < 0:
            self.add_error('quantity', forms.ValidationError("Quantity should not be negative."))

        if price is not None and price < 0:
            self.add_error('price', forms.ValidationError("Price should not be negative."))

        if discount is not None and discount < 0:
            self.add_error('discount', forms.ValidationError("Discount should not be negative."))

        return cleaned_data