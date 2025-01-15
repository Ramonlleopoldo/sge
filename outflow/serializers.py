from rest_framework import serializers
from . import models


class OutflowSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Outflow
        fields = '__all__'