"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
from django.utils.translation import gettext_lazy as _

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
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

class Greenhouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.FloatField(help_text="Size in square meters")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SensorData(models.Model):
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    luminosity = models.FloatField()
    CO2_level = models.FloatField()
    soil_moisture = models.FloatField()
    pH = models.FloatField(null=True, blank=True)
    nutrient_level = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for {self.greenhouse.name} at {self.timestamp}"

class ActuatorStatus(models.Model):
    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    irrigation_status = models.BooleanField()
    lighting_status = models.BooleanField()
    ventilation_status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Actuator status for {self.greenhouse.name} at {self.timestamp}"

class Alert(models.Model):
    ALERT_CHOICES = [
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
    STATUS_CHOICES = [
        ('UN', 'Unacknowledged'),
        ('AC', 'Acknowledged'),
        ('RE', 'Resolved'),
        ('CL', 'Closed')
    ]

    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=2, choices=ALERT_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.get_alert_type_display()} for {self.greenhouse.name} at {self.timestamp}"
