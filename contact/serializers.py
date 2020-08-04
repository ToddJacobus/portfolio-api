from rest_framework import serializers

from core.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """serializer for Contact objects"""

    class Meta:
        model = Contact
        fields = (id, name, email, comments)
        