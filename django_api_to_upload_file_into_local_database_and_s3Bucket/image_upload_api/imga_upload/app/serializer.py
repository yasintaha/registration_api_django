from rest_framework import serializers
from .models import file_model

class file_serializer(serializers.ModelSerializer):

    class Meta():
        model = file_model
        fields = ('file','key','timestamp')