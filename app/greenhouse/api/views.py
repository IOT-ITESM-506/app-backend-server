"""Views for the greenhouse API."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from core.models import (
    Greenhouse,
    SensorRecord,
    ActuatorStatus,
    Alert,
)
from greenhouse.api.serializers import (
    GreenhouseSerializer,
    SensorRecordSerializer,
    ActuatorStatusSerializer,
    AlertSerializer,
)

class GreenhouseViewSet(viewsets.ModelViewSet):
    """Manage greenhouse in the database."""
    serializer_class = GreenhouseSerializer
    queryset = Greenhouse.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific greenhouse by name."""
        name = kwargs.get('pk')
        greenhouses = self.queryset.filter(name__icontains=name, user=request.user)
        serializer = self.get_serializer(greenhouses, many=True)
        return Response(serializer.data)

    
    def perform_create(self, serializer):
        """Create a new greenhouse."""
        serializer.save(user=self.request.user)

class SensorRecordViewSet(viewsets.ModelViewSet):
    """Manage sensor records in the database."""
    serializer_class = SensorRecordSerializer
    queryset = SensorRecord.objects.all()
    permission_classes = [IsAuthenticated]
    
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

class ActuatorStatusViewSet(viewsets.ModelViewSet):
    """Manage actuator statuses in the database."""
    serializer_class = ActuatorStatusSerializer
    queryset = ActuatorStatus.objects.all()
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        """Create a new actuator status."""
        serializer.save()


