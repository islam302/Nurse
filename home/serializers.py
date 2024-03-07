from .models import test
from rest_framework import serializers


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'