"""Views for the greenhouse API."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.response import Response

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

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a greenhouse by ID with user filter."""
        instance = self.get_object()
        user = self.request.query_params.get('user', None)

        if user and instance.user != user:
            raise Http404("No se encontró el invernadero con el ID proporcionado para el usuario especificado")

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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