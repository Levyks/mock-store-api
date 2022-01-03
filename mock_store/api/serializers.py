from .models import Category, Product, User
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user