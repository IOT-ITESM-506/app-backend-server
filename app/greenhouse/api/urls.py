"""URLS for the greenhouse API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from greenhouse.api import views

router = DefaultRouter()
router.register('greenhouse', views.GreenhouseViewSet, basename='greenhouse')
router.register('sensor-record', views.SensorRecordViewSet, basename='sensor-record')
router.register("alerts", views.AlertViewSet, basename="alerts")

app_name = 'greenhouse'

urlpatterns = [
    path('', include(router.urls))
]   