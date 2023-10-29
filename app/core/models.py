from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class UserManager(BaseUserManager):
    """Manager for users."""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    greenhouses = models.ManyToManyField('Greenhouse', blank=True, related_name='user_greenhouses')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class Greenhouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.FloatField(help_text="Size in square meters")
    greenhouse_description = models.TextField(blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='greenhouse_users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SensorRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, related_name='sensor_records')
    temperature = models.FloatField()
    humidity = models.FloatField()
    luminosity = models.FloatField()
    CO2_level = models.FloatField()
    soil_moisture = models.FloatField()
    pH = models.FloatField(null=True, blank=True)
    nutrient_level = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sensor_records', on_delete=models.CASCADE)

    def __str__(self):
        return f"Data for {self.greenhouse.name} at {self.timestamp}"

class ActuatorStatus(models.Model):
    REQUIRED_ACTION = [
        ('IRR', 'Irrigation'),
        ('LIG', 'Lighting'),
        ('VEN', 'Ventilation'),
    ]
    ACTUATOR_STATUS = [
        ('PEN', 'Pending'),
        ('RUN', 'Running'),
        ('FIN', 'Finished'),
        ('ERR', 'Error'),
        
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, related_name='actuator_statuses')
    required_action = models.CharField(max_length=3, choices=REQUIRED_ACTION)
    timestamp = models.DateTimeField(auto_now_add=True)
    actuator_status = models.CharField(max_length=3, choices=ACTUATOR_STATUS)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actuator_statuses', on_delete=models.CASCADE)

    def __str__(self):
        return f"Actuator status for {self.greenhouse.name} at {self.timestamp}"

class Alert(models.Model):
    ALERT_TYPE_OPTIONS = [
        ('HT', 'High Temperature'),
        ('LL', 'Low Luminosity'),
        ('HM', 'High Humidity'),
        ('LM', 'Low Humidity'),
        ('HC', 'High CO2 Level'),
        ('LC', 'Low CO2 Level'),
        ('SM', 'Soil Moisture'),
        ('PH', 'pH Level'),
        ('NL', 'Nutrient Level'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=2, choices=ALERT_TYPE_OPTIONS)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='alerts', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_alert_type_display()} for {self.greenhouse.name} at {self.timestamp}"
