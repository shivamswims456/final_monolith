# Generated by Django 4.1.5 on 2023-02-28 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0007_rename_ert_good_ert1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='ert1',
            new_name='ert',
        ),
    ]
