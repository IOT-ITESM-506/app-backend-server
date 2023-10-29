"""Views for the greenhouse API."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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

class ActuatorStatusViewSet(viewsets.ModelViewSet):
    """Manage actuator statuses in the database."""
    serializer_class = ActuatorStatusSerializer
    queryset = ActuatorStatus.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def perform_create(self, serializer):
        """Create a new actuator status."""
        serializer.save(user=self.request.user)


class AlertViewSet(viewsets.ModelViewSet):
    """Manage alerts in the database."""
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def perform_create(self, serializer):
        """Create a new alert."""
        serializer.save(user=self.request.user)