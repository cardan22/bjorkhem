# Generated by Django 4.2.7 on 2023-12-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=254, null=True),
        ),
    ]
