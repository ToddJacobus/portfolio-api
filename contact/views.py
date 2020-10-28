from rest_framework import viewsets, mixins

from core.models import Contact
from contact import serializers
from core.tasks import send_submission_notice


class ContactVewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """A simple write-only viewset"""
    serializer_class = serializers.ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        """create a new contact entry"""
        send_submission_notice(**serializer.validated_data)

        serializer.save()