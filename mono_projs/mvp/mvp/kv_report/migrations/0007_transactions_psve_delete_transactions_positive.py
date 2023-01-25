# Generated by Django 4.1.4 on 2023-01-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv_report', '0006_alter_warehouse_total_warehouse_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions_psve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.PositiveBigIntegerField()),
                ('type', models.TextField(max_length=30)),
                ('bill_date', models.DateField()),
                ('bill_item', models.PositiveBigIntegerField()),
                ('item_qty', models.FloatField()),
                ('item_total', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='transactions_positive',
        ),
    ]
