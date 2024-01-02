from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=80, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)


    def __str__(self):
        return self.user.username


class GDPRConsent(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    gdpr_consent = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile and GDPRConsent
    """
    user_profile, _ = UserProfile.objects.get_or_create(user=instance)

    # Create or update GDPRConsent instance
    gdpr_consent, _ = GDPRConsent.objects.get_or_create(user_profile=user_profile)

    # Save profile
    user_profile.save()

    # Save GDPRConsent instance
    gdpr_consent.save()