# Generated by Django 4.0.10 on 2023-10-12 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Greenhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('size', models.FloatField(help_text='Size in square meters')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('luminosity', models.FloatField()),
                ('CO2_level', models.FloatField()),
                ('soil_moisture', models.FloatField()),
                ('pH', models.FloatField(blank=True, null=True)),
                ('nutrient_level', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.greenhouse')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('HT', 'High Temperature'), ('LL', 'Low Luminosity'), ('HM', 'High Humidity'), ('LM', 'Low Humidity'), ('HC', 'High CO2 Level'), ('LC', 'Low CO2 Level'), ('SM', 'Soil Moisture'), ('PH', 'pH Level'), ('NL', 'Nutrient Level')], max_length=2)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('UN', 'Unacknowledged'), ('AC', 'Acknowledged'), ('RE', 'Resolved'), ('CL', 'Closed')], max_length=2)),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.greenhouse')),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irrigation_status', models.BooleanField()),
                ('lighting_status', models.BooleanField()),
                ('ventilation_status', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.greenhouse')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='greenhouses',
            field=models.ManyToManyField(blank=True, to='core.greenhouse'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
