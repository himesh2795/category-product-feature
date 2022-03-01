from rest_framework import serializers

from modelcore.models.ProductModel import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"
