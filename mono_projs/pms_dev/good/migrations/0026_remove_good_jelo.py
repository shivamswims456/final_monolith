# Generated by Django 4.1.5 on 2023-03-02 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0025_good_jelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='jelo',
        ),
    ]
