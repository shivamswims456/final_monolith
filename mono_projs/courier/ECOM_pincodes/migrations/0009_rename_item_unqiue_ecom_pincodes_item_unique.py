# Generated by Django 4.1.5 on 2023-02-05 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECOM_pincodes', '0008_alter_ecom_pincodes_city_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ecom_pincodes',
            old_name='item_unqiue',
            new_name='item_unique',
        ),
    ]
