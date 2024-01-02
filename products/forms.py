from django import forms
from .models import Product, Category, Stock


class ProductForm(forms.ModelForm):
    """ 
    Form for creating and updating Product instances, 
    including stock information.
    """

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'favorites': forms.HiddenInput(),
        }

    # Add quantity field for stock information
    quantity = forms.IntegerField(label='Quantity in Stock', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
