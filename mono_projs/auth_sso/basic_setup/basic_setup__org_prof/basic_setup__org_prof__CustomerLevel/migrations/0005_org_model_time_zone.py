# Generated by Django 4.1.5 on 2023-03-17 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_setup', '0005_city__prnts_associated_countries__prnts_associated_and_more'),
        ('basic_setup__org_prof__CustomerLevel', '0004_org_model_org_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='org_model',
            name='time_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.time_zones'),
        ),
    ]