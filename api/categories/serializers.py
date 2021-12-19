from rest_framework import serializers

from core.models import Product, Category, ItemImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'categories',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = [
            'image',
        ]
