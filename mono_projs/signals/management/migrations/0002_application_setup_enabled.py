# Generated by Django 4.1.5 on 2023-01-29 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application_setup',
            name='enabled',
            field=models.BooleanField(default='1'),
            preserve_default=False,
        ),
    ]