# Generated by Django 2.2.4 on 2021-03-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HangarAndMechlabApp', '0006_auto_20210304_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='chassis',
            name='tons_engine',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
            preserve_default=False,
        ),
    ]
