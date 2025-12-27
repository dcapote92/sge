from rest_framework.serializers import ModelSerializer
from . import models


class BrandSerializer(ModelSerializer):
    
    class Meta:
        model = models.Brand
        fields = '__all__'