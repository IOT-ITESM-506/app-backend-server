"""URLS for the greenhouse API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from greenhouse.api import views

router = DefaultRouter()
router.register('greenhouse', views.GreenhouseViewSet)
router.register('sensor-record', views.SensorRecordViewSet)
router.register('actuator-status', views.ActuatorStatusViewSet)

app_name = 'greenhouse'

urlpatterns = [
    path('', include(router.urls))
]   