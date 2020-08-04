from rest_framework import viewsets

from core.models import Contact

class ContactVewSet(viewsets.ModelViewSet):
    """A simple, write-only viewset"""
    serializer_class = serializers.ContactSerializer

    def perform_create(self, serializer):
        """create a new contact entry"""
        serializer.save()