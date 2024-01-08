# Generated by Django 4.2.7 on 2024-01-02 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_gdpr_consent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gdpr_consent',
        ),
        migrations.CreateModel(
            name='GDPRConsent',
            fields=[
                (
                    'id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                    )
                ),
                ('gdpr_consent', models.BooleanField(default=False)),
                ('user_profile', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='profiles.userprofile'
                )
                ),
            ],
        ),
    ]
