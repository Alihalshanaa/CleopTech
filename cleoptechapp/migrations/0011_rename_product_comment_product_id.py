# Generated by Django 4.1.4 on 2023-01-06 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleoptechapp', '0010_rename_product_comment_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='product',
            new_name='product_id',
        ),
    ]