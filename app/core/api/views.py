from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

class HealthCheckView(GenericAPIView):
    """A simple APIView that reports if the service is healthy."""
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, data={'status': 'healthy'})