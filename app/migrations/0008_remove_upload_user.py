# Generated by Django 5.0.2 on 2024-03-06 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_upload_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
    ]
