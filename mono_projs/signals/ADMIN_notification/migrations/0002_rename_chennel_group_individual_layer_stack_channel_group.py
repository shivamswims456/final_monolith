# Generated by Django 4.1.5 on 2023-01-29 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN_notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individual_layer_stack',
            old_name='chennel_group',
            new_name='channel_group',
        ),
    ]