from rest_framework import serializers
from .models import Plants

class PlatsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_image = serializers.CharField(max_length=200000000000000000000000)

    class Meta:
        model = Plants
        fields = ('__all__')