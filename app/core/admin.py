from django.contrib import admin
from core.models import User, Greenhouse, SensorRecord, Alert

admin.site.register(User)
admin.site.register(Greenhouse)
admin.site.register(SensorRecord)
admin.site.register(Alert)