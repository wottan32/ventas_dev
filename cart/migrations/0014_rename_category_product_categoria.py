# Generated by Django 3.2.3 on 2021-06-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_product_peso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categoria',
        ),
    ]
