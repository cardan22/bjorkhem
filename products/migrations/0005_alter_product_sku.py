# Generated by Django 4.2.7 on 2023-12-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_discount_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='L7WSD9K8', max_length=254, unique=True),
        ),
    ]