# Generated by Django 4.1.5 on 2023-01-29 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN_notification', '0002_rename_chennel_group_individual_layer_stack_channel_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual_layer_stack',
            name='accessible_till',
        ),
    ]