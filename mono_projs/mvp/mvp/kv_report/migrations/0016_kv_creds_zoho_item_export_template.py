# Generated by Django 4.1.4 on 2023-01-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv_report', '0015_warehouse_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='kv_creds',
            name='zoho_item_export_template',
            field=models.PositiveBigIntegerField(default=536460000019384462),
            preserve_default=False,
        ),
    ]
