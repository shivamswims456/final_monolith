# Generated by Django 4.1.5 on 2023-03-02 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0023_good_jelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='jelo',
        ),
    ]
