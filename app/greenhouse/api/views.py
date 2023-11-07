"""Views for the greenhouse API."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


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

    def get_queryset(self):
        sensor_record_circuit_id = self.request.query_params.get('sensor_record_circuit_id', None)
        user = self.request.query_params.get('user', None)

        if not sensor_record_circuit_id and not user:
            raise Http404("Debe proporcionar al menos un parámetro de filtrado")

        queryset = Greenhouse.objects.all()
        if sensor_record_circuit_id:
            queryset = queryset.filter(sensor_record_circuit_id=sensor_record_circuit_id)
        if user:
            queryset = queryset.filter(user=user)
        if not queryset.exists():
            raise Http404("No se encontraron invernaderos con los parámetros proporcionados")

        return queryset

    def perform_create(self, serializer):
        """Create a new greenhouse."""
        serializer.save()

class SensorRecordViewSet(viewsets.ModelViewSet):
    """Manage sensor records in the database."""
    serializer_class = SensorRecordSerializer
    queryset = SensorRecord.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve sensor records for authenticated user."""
        return self.queryset.filter(greenhouse__user=self.request.user)
    
    def perform_create(self, serializer):
        """Create a new sensor record."""
        self.permission_classes = []
        serializer.save()
        self.permission_classes = [IsAuthenticated]

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


