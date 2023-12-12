from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_full_name': 'Full Name',
            'default_address1': 'Address 1',
            'default_address2': 'Address 2',
            'default_postcode': 'Postcode',
            'default_city': 'City',
            'default_phone_number': 'Phone Number',
        }

        for field_name, placeholder_text in placeholders.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholder_text
            self.fields[field_name].label = False

        # Add gdpr_consent field to the form
        self.fields['gdpr_consent'] = forms.BooleanField(
            required=True,
            label='I agree to the GDPR terms and conditions. My data will only be stored to enhance the shopping experience.',
            widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        )

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
