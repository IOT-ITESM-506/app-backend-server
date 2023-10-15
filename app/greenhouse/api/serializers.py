"""Serializer for the greenhouse app."""
from rest_framework import serializers
from core.models import Greenhouse

class GreenhouseSerializer(serializers.ModelSerializer):
    """Serializer for the greenhouse object."""
    class Meta:
        model = Greenhouse
        fields = '__all__'
        read_only_fields = ('id',)