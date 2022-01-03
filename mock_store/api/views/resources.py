from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework import generics, permissions
from rest_framework.response import Response

from ..models import Category, Product
from ..serializers import CategorySerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    paginator = None


class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(APIView):

    queryset = Product.objects.all()
    paginator = api_settings.DEFAULT_PAGINATION_CLASS()
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get(self, request, format=None):

        products = self.queryset
        
        categories = request.GET.getlist('categories[]')
        if categories:
            products = products.filter(categories__pk__in=categories)

        search_query = request.GET.get('search')
        if search_query:
            products = products.filter(name__icontains=search_query)

        products = products.order_by('-updated_at')

        page = self.paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(
            page, context={'request': request}, many=True)

        return self.paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):

        print("User: ", request.user)

        return Response("Not implemented yet")


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
