# Generated by Django 4.1.4 on 2023-01-06 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleoptechapp', '0013_alter_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='productid',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='userid',
            new_name='user',
        ),
    ]