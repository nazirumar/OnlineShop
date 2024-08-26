from django.shortcuts import get_object_or_404
from api.serializers import CategorySerializer, ProductSerializer
from rest_framework import generics, viewsets
from django.db.models import Count, Max
from api.pagination import StandardPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from api.pagination import StandardPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from shop.models import Category, Product
# Create your views here.


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.annotate(total_product=Count('product') )
    serializer_class = CategorySerializer
    pagination_class = StandardPagination


class CategoryDetailViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.annotate(total_product=Count('product'))
    serializer_class = CategorySerializer


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardPagination


class ProductCreateView(APIView):
    queryset = Product.objects.all()  # Add queryset attribute
    authentication_classes = [BasicAuthentication], # Add authentication_classes attribute
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        return Response({
            'product_id': product.id,
            'product_name': product.name,
            'product_description': product.description,
            # Add other fields as necessary
        })
    def post(self, request, pk, format=None):
        product = get_object_or_404(Product, pk=pk)
        product.user=request.user
        product.save()
        return Response({'Add To like': True})