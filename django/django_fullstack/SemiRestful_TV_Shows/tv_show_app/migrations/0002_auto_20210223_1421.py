# Generated by Django 2.2.4 on 2021-02-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='release_date',
            field=models.DateField(),
        ),
    ]