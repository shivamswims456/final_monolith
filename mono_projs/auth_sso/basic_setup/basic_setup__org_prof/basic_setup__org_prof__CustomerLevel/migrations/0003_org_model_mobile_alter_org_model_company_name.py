# Generated by Django 4.1.5 on 2023-03-15 18:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('basic_setup__org_prof__CustomerLevel', '0002_org_model_delete_geocombination'),
    ]

    operations = [
        migrations.AddField(
            model_name='org_model',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+919693432136', max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='org_model',
            name='company_name',
            field=models.CharField(max_length=120),
        ),
    ]
