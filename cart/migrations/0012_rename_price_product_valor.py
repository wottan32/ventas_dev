# Generated by Django 3.2.3 on 2021-06-22 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_rename_description_product_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='valor',
        ),
    ]
