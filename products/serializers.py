from rest_framework import serializers
from .models import Condutor

class CondutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condutor
        fields = '__all__'