"""Serializer for the greenhouse app."""
from rest_framework import serializers
from core.models import Greenhouse, SensorRecord, ActuatorStatus, Alert

class GreenhouseSerializer(serializers.ModelSerializer):
    """Serializer for the greenhouse object."""
    class Meta:
        model = Greenhouse
        fields = '__all__'
        read_only_fields = ('id',)


class SensorRecordSerializer(serializers.ModelSerializer):
    """Serializer for the sensor record object."""
    class Meta:
        model = SensorRecord
        fields = '__all__'
        read_only_fields = ('id',)


class ActuatorStatusSerializer(serializers.ModelSerializer):
    """Serializer for the actuator status object."""
    class Meta:
        model = ActuatorStatus
        fields = '__all__'
        read_only_fields = ('id',)


class AlertSerializer(serializers.ModelSerializer):
    """Serializer for the alert object."""
    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ('id',)