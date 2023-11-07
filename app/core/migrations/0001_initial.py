# Generated by Django 4.0.10 on 2023-11-07 01:48

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
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('greenhouse_role', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Greenhouse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('size', models.FloatField(help_text='Size in square meters')),
                ('greenhouse_description', models.TextField(blank=True)),
                ('logo', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('sensor_record_circuit_id', models.UUIDField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greenhouse_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SensorRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('luminosity', models.FloatField()),
                ('CO2_level', models.FloatField()),
                ('soil_moisture', models.FloatField()),
                ('pH', models.FloatField(blank=True, null=True)),
                ('nutrient_level', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_records', to='core.greenhouse')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('alert_type', models.CharField(choices=[('HT', 'High Temperature'), ('LL', 'Low Luminosity'), ('HM', 'High Humidity'), ('LM', 'Low Humidity'), ('HC', 'High CO2 Level'), ('LC', 'Low CO2 Level'), ('SM', 'Soil Moisture'), ('PH', 'pH Level'), ('NL', 'Nutrient Level'), ('OT', 'Other'), ('NA', 'N/A'), ('UN', 'Unknown'), ('ER', 'Error')], max_length=2)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sensor_record_circuit_id', models.UUIDField()),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='core.greenhouse')),
            ],
        ),
        migrations.CreateModel(
            name='ActuatorStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('required_action', models.CharField(choices=[('IRR', 'Irrigation'), ('LIG', 'Lighting'), ('VEN', 'Ventilation')], max_length=3)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('actuator_status', models.CharField(choices=[('PEN', 'Pending'), ('RUN', 'Running'), ('FIN', 'Finished'), ('ERR', 'Error')], max_length=3)),
                ('sensor_record_circuit_id', models.UUIDField()),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actuator_statuses', to='core.greenhouse')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='greenhouses',
            field=models.ManyToManyField(blank=True, related_name='user_greenhouses', to='core.greenhouse'),
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
