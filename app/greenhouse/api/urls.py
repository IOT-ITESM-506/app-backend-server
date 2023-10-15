"""URLS for the greenhouse API."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from greenhouse.api import views

router = DefaultRouter()
router.register('greenhouse', views.GreenhouseViewSet)

app_name = 'greenhouse'

urlpatterns = [
    path('', include(router.urls))
]   