# Generated by Django 4.1.5 on 2023-03-03 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modification_logs', '0001_initial'),
        ('organisations', '0002_bi_organisations_users_f_organisation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='I_organisations_users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modification_log', models.ManyToManyField(to='modification_logs.modification_logs')),
            ],
        ),
        migrations.AddField(
            model_name='f_organisation',
            name='modification_log',
            field=models.ManyToManyField(to='modification_logs.modification_logs'),
        ),
        migrations.AddField(
            model_name='f_organisation',
            name='org_admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='f_organisation',
            name='employee_count',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.DeleteModel(
            name='BI_organisations_users',
        ),
        migrations.AddField(
            model_name='i_organisations_users',
            name='organisations',
            field=models.ManyToManyField(to='organisations.f_organisation'),
        ),
        migrations.AddField(
            model_name='i_organisations_users',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
