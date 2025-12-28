from rest_framework.serializers import ModelSerializer
from . import models


class InflowSerializer(ModelSerializer):

    class Meta:
        model = models.Inflow
        fields = '__all__'
