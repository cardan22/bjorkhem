from django import forms
from .models import UserProfile, GDPRConsent


class UserProfileForm(forms.ModelForm):
    gdpr_consent = forms.BooleanField(
        required=True,
        label='I agree to the GDPR terms and conditions. My data will only be stored to enhance the shopping experience.',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

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
            'default_phone_number': 'Phone Number',
            'default_address1': 'Address 1',
            'default_address2': 'Address 2',
            'default_postcode': 'Postcode',
            'default_city': 'City',
        }

        for field_name, placeholder_text in placeholders.items():
            self.fields[field_name].widget.attrs['placeholder'] = placeholder_text
            self.fields[field_name].label = False

        self.fields['default_full_name'].widget.attrs['autofocus'] = True

    def save(self, commit=True):
        """
        Save the UserProfile and associated GDPRConsent.
        """
        user_profile = super().save(commit=False)

        if commit:
            user_profile.save()

        gdpr_consent, _ = GDPRConsent.objects.get_or_create(user_profile=user_profile)
        gdpr_consent.gdpr_consent = self.cleaned_data['gdpr_consent']

        try:
            gdpr_consent.save()
        except Exception as e:
            pass

        return user_profile
