# Generated by Django 4.1.5 on 2023-03-20 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_setup__user_prof', '0001_initial'),
        ('basic_setup', '0008_date_time_format_alter_time_zones_difference'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=60)),
                ('Isonline', models.BooleanField()),
                ('street', models.TextField(max_length=150)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('dob', models.DateField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.countries')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_created_by', to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.currency')),
                ('date_time_format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.date_time_format')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.state')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup__user_prof.user_statues')),
                ('time_zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.time_zones')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_updated_by', to=settings.AUTH_USER_MODEL)),
                ('zip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='basic_setup.zip')),
            ],
        ),
    ]