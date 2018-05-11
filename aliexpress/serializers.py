from rest_framework import serializers
from aliexpress.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'name', 'tech_name')


class ProductSerializer(serializers.ModelSerializer):
    pictures = serializers.SlugRelatedField(many=True, slug_field='url', read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('ali_id', 'pictures', 'name', 'description', 'preview_url', 'currency', 'price', 'category')
