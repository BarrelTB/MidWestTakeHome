from rest_framework import serializers
from .models import LoremIpsum, Contact

class LoremIpsumSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoremIpsum
        fields = [
            'title',
            'text',
            'img',
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'firstName',
            'lastName',
            'title',
            'email',
            'message',
        ]