# Generated by Django 4.1.5 on 2023-03-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0012_remove_good_jelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='jelo',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
