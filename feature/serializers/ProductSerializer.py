from rest_framework import serializers

from modelcore.models.ProductModel import ProductModel
from feature.serializers.CategorySerializer import CategorySerializer


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = ProductModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"
