# Generated by Django 4.1.5 on 2023-03-15 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_setup', '0002_alter_city__chlds_included_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='currency_name',
            new_name='name',
        ),
    ]
