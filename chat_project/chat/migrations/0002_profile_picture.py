# Generated by Django 5.0.4 on 2024-04-04 14:51

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=chat.models.user_directory_path),
        ),
    ]
