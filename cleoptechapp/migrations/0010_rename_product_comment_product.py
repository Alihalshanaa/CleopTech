# Generated by Django 4.1.4 on 2023-01-06 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleoptechapp', '0009_product_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Product',
            new_name='product',
        ),
    ]
