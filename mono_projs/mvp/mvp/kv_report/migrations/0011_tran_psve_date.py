# Generated by Django 4.1.4 on 2023-01-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv_report', '0010_tran_psve_delete_bill_fetches_delete_billitem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tran_psve',
            name='date',
            field=models.DateTimeField(default='2020-12-12'),
            preserve_default=False,
        ),
    ]
