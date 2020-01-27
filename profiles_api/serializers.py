from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    ''' serializes  a name field for testing apiview'''

    name = serializers.CharField(max_length=10)
