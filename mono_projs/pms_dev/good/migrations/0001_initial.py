# Generated by Django 4.1.5 on 2023-02-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=30)),
                ('ert1', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]