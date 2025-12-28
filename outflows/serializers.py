from rest_framework.serializers import ModelSerializer
from . import models


class OutflowSerializer(ModelSerializer):

    class Meta:
        model = models.Outflow
        fields = '__all__'
