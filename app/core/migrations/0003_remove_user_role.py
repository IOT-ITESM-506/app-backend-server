# Generated by Django 4.0.10 on 2023-11-23 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_sensorrecord_temperature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]