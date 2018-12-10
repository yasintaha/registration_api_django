from rest_framework import serializers
from app.models import Register_model

class Register_Serializer(serializers.ModelSerializer):
    class Meta():
        model = Register_model
        fields = '__all__'
