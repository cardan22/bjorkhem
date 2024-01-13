from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, GDPRConsent


class UserProfileModelTest(TestCase):
    def test_user_profile_creation(self):
        # Create a user
        user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

        # Check if UserProfile is created
        user_profile = UserProfile.objects.get(user=user)
        self.assertIsNotNone(user_profile)
        self.assertEqual(user_profile.user, user)
        self.assertIsNone(user_profile.default_full_name)
        self.assertIsNone(user_profile.default_phone_number)
        self.assertIsNone(user_profile.default_address1)
        self.assertIsNone(user_profile.default_address2)
        self.assertIsNone(user_profile.default_postcode)
        self.assertIsNone(user_profile.default_city)

        # Check if GDPRConsent is created
        gdpr_consent = GDPRConsent.objects.get(user_profile=user_profile)
        self.assertIsNotNone(gdpr_consent)
        self.assertEqual(gdpr_consent.user_profile, user_profile)
        self.assertFalse(gdpr_consent.gdpr_consent)
