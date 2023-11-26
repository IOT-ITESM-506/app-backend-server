"""Views for the greenhouse API."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response
from rest_framework import filters

from core.models import (
    Greenhouse,
    SensorRecord,
    Alert,
)
from greenhouse.api.serializers import (
    GreenhouseSerializer,
    SensorRecordSerializer,
    AlertSerializer,
)

class GreenhouseViewSet(viewsets.ModelViewSet):
    """Manage greenhouse in the database."""
    serializer_class = GreenhouseSerializer
    queryset = Greenhouse.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'user__id', 'microcontroller_mac_address']

    def perform_create(self, serializer):
        """Create a new greenhouse."""
        serializer.save()


class SensorRecordViewSet(viewsets.ModelViewSet):
    """Manage sensor records in the database."""
    serializer_class = SensorRecordSerializer
    queryset = SensorRecord.objects.all()
    
    def perform_create(self, serializer):
        """Create a new sensor record."""
        serializer.save()

class AlertViewSet(viewsets.ModelViewSet):
    """Manage alerts in the database."""
    serializer_class = AlertSerializer
    queryset = Alert.objects.all().order_by('-id')
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """Create a new alert."""
        serializer.save()