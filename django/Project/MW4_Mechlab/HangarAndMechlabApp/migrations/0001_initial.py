# Generated by Django 2.2.4 on 2021-03-03 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('dmgType', models.TextField()),
                ('slotSpace', models.IntegerField()),
                ('tons', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('eSlots', models.IntegerField()),
                ('bSlots', models.IntegerField()),
                ('mSlots', models.IntegerField()),
                ('oSlots', models.IntegerField()),
                ('equips', models.ManyToManyField(related_name='assigned_parts', to='HangarAndMechlabApp.Equip')),
            ],
        ),
        migrations.CreateModel(
            name='Chassis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('tons', models.IntegerField()),
                ('tot_eSlots', models.IntegerField()),
                ('tot_bSlots', models.IntegerField()),
                ('tot_mSlots', models.IntegerField()),
                ('tot_oSlots', models.IntegerField()),
                ('hangar_src', models.TextField()),
                ('mechlab_src', models.TextField()),
                ('parts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechs', to='HangarAndMechlabApp.Part')),
            ],
        ),
    ]
