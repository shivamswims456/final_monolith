# Generated by Django 4.1.5 on 2023-03-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_setup__org_prof__CustomerLevel', '0003_org_model_mobile_alter_org_model_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='org_model',
            name='org_id',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
