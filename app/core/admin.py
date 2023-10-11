from django.contrib import admin
from core.models import User, Greenhouse, SensorData, ActuatorStatus, Alert

# Register your models here.

admin.site.register(User)
admin.site.register(Greenhouse)
admin.site.register(SensorData)
admin.site.register(ActuatorStatus)
admin.site.register(Alert)