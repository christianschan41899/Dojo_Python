# Generated by Django 2.2.4 on 2021-03-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HangarAndMechlabApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip',
            name='tons',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
