# Generated by Django 4.1.4 on 2023-01-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv_report', '0002_kv_creds_zoho_org_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='billItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemId', models.PositiveBigIntegerField()),
                ('productId', models.PositiveBigIntegerField()),
                ('itemName', models.TextField(max_length=150)),
                ('qty', models.FloatField()),
                ('subTotal', models.FloatField()),
                ('total', models.FloatField()),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='transactions_positive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billId', models.PositiveBigIntegerField()),
                ('type', models.TextField(max_length=30)),
                ('billNumber', models.TextField(max_length=50)),
                ('biilDate', models.DateField()),
                ('billStatus', models.TextField(max_length=30)),
                ('total_bcy', models.FloatField()),
                ('total_sub_bcy', models.FloatField()),
                ('vendor_id', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='warehouseTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.PositiveIntegerField()),
                ('warehouse_id', models.PositiveBigIntegerField()),
                ('warehouse_name', models.TextField(max_length=150)),
                ('status', models.TextField(max_length=30)),
                ('status_formatted', models.TextField(max_length=30)),
                ('warehouse_stock_on_hand', models.FloatField()),
                ('initial_stock', models.FloatField()),
                ('initial_stock_rate', models.FloatField()),
                ('warehouse_available_stock', models.FloatField()),
                ('warehouse_actual_available_stock', models.FloatField()),
                ('warehouse_committed_stock', models.FloatField()),
                ('warehouse_actual_committed_stock', models.FloatField()),
                ('warehouse_available_for_sale_stock', models.FloatField()),
                ('warehouse_actual_available_for_sale_stock', models.FloatField()),
            ],
        ),
    ]
