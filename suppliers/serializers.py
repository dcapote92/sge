from rest_framework.serializers import ModelSerializer
from . import models


class SupplierSerializer(ModelSerializer):
    
    class Meta:
        model = models.Supplier
        fields = '__all__'