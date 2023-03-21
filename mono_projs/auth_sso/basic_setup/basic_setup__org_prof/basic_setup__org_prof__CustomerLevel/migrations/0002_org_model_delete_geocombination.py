# Generated by Django 4.1.5 on 2023-03-15 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('basic_setup', '0003_rename_currency_name_currency_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_setup__org_prof__CustomerLevel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='org_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=150)),
                ('street', models.TextField(max_length=150)),
                ('alias', models.TextField(max_length=150)),
                ('employee_count', models.PositiveIntegerField()),
                ('website', models.URLField()),
                ('company_name', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('primary_email', models.EmailField(max_length=254)),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.countries')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.currency')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.state')),
                ('zip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.zip')),
            ],
        ),
        migrations.DeleteModel(
            name='geoCombination',
        ),
    ]