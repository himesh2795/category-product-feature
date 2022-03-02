from rest_framework import serializers
from modelcore.models.CategoryModel import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'name', 'parent')


class CategoryTreeSerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'parent', 'subcategories']
