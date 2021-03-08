from rest_framework.serializers import ModelSerializer
from .models import Messages, Requests


class MessagesSerializer(ModelSerializer):
    class Meta:
        model = Messages

    def create(self, validated_data):
        message = super().create(validated_data)
        message.save()
        return message


class RequestsSerializer(ModelSerializer):
    class Meta:
        model = Requests

    def create(self, validated_data):
        request = super().create(validated_data)
        request.save()
        return request
