# Generated by Django 2.2.4 on 2021-02-26 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration', '0001_initial'),
        ('comment_wall_app', '0002_messageblock_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contained_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment_users', models.ManyToManyField(related_name='comments', to='login_and_registration.User')),
                ('parent_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_comments', to='comment_wall_app.MessageBlock')),
            ],
        ),
    ]
