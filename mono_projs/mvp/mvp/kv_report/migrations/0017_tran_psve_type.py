# Generated by Django 4.1.4 on 2023-01-12 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv_report', '0016_kv_creds_zoho_item_export_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='tran_psve',
            name='type',
            field=models.TextField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
