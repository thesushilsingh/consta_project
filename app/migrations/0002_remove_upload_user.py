# Generated by Django 5.0.2 on 2024-03-06 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='user',
        ),
    ]