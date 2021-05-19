# Generated by Django 2.2.4 on 2021-03-04 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HangarAndMechlabApp', '0005_auto_20210304_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chassis',
            name='parts',
        ),
        migrations.AddField(
            model_name='chassis',
            name='tons_armor',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='mech',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='HangarAndMechlabApp.Chassis'),
            preserve_default=False,
        ),
    ]