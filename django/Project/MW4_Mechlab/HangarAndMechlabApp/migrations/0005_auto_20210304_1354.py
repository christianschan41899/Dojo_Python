# Generated by Django 2.2.4 on 2021-03-04 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HangarAndMechlabApp', '0004_auto_20210304_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='displaychassis',
            old_name='hanagar_src',
            new_name='hangar_src',
        ),
    ]
