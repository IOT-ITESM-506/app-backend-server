# Generated by Django 4.0.10 on 2023-10-14 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greenhouse',
            name='email',
        ),
    ]
