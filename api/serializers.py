from rest_framework import serializers
from shop.models import Category, Product
from django.db.models import Count


class CategorySerializer(serializers.ModelSerializer):
    total_product = serializers.IntegerField()
    popular_products = serializers.SerializerMethodField()

    def get_popular_products(self, obj):
        products = obj.product.annotate(total_category=Count("category")).order_by(
            "total_category"
        )[:3]
        return [f"{c.name}  ({c.total_category})" for c in products]

    class Meta:
        model = Category
        fields = [
            "pk",
            "name",
            "slug",
            "total_product",
            "popular_products",
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "pk",
            "name",
            "slug",
            'user',
            "description",
            "image",
            "price",
            "available",
            "created",
            "updated",
        ]
