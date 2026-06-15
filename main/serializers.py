from rest_framework.serializers import ModelSerializer
from .models import HelloWorldModel


class HelloWorldSerializer(ModelSerializer):
    class Meta:
        model = HelloWorldModel
        fields = ["title", "image"]