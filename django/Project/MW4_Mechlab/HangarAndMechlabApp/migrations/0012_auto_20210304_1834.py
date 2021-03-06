# Generated by Django 2.2.4 on 2021-03-05 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HangarAndMechlabApp', '0011_auto_20210304_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='templatepart_ptr',
        ),
        migrations.RemoveField(
            model_name='templatepart',
            name='mech',
        ),
        migrations.AddField(
            model_name='part',
            name='bSlots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='eSlots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='mSlots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='mech',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='HangarAndMechlabApp.Chassis'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='part',
            name='oSlots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='templatepart',
            name='displayedMech',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='displayedParts', to='HangarAndMechlabApp.displayChassis'),
            preserve_default=False,
        ),
    ]
