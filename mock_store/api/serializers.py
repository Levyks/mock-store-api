from .models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'categories')
