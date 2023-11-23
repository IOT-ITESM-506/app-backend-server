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
    greenhouse_role = models.CharField(max_length=255, blank=True)

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
    logo = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)

    microcontroller_mac_address = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='greenhouse_users', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SensorRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    humidity = models.FloatField()
    luminosity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, related_name='sensor_records')

    def __str__(self):
        return f"Data for {self.greenhouse.name} at {self.timestamp}"

class Alert(models.Model):
    ALERT_TYPE_OPTIONS = [
        ('HT', 'High Temperature'),
        ('LL', 'Low Luminosity'),
        ('HM', 'High Humidity'),
        ('LM', 'Low Humidity'),
        ('OT', 'Other'),
        ('NA', 'N/A'),
        ('UN', 'Unknown'),
        ('ER', 'Error'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alert_type = models.CharField(max_length=2, choices=ALERT_TYPE_OPTIONS)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    greenhouse = models.ForeignKey(Greenhouse, on_delete=models.CASCADE, related_name='alerts')

    def __str__(self):
        return f"{self.get_alert_type_display()} for {self.greenhouse.name} at {self.timestamp}"