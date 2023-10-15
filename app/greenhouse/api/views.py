"""Views for the greenhouse API."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Greenhouse
from greenhouse.api.serializers import GreenhouseSerializer

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