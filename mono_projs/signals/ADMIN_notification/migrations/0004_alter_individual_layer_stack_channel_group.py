# Generated by Django 4.1.5 on 2023-01-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADMIN_notification', '0003_remove_individual_layer_stack_accessible_till'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual_layer_stack',
            name='channel_group',
            field=models.TextField(max_length=12),
        ),
    ]