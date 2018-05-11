from django.http import Http404
from django.shortcuts import render, redirect

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from aliexpress.models import Product, Category
from aliexpress.serializers import ProductSerializer, CategorySerializer


class ProductsList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.filter(is_published=True).order_by('-publish_dt')
        category_name = self.kwargs.get('category_name')
        if category_name:
            categories = Category.objects.filter(tech_name=category_name).values_list('id', flat=True)
            if categories.exists():
                qs = qs.filter(category_id__in=categories)
            else:
                raise Http404
        return qs


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'ali_id'


class CategoriesPageNumberPagination(PageNumberPagination):
    page_size = 100


class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all().order_by('tech_name').distinct('tech_name')
    serializer_class = CategorySerializer
    pagination_class = CategoriesPageNumberPagination


class FilterByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'category_id'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        if not category_name:
            return

        try:
            category = Category.objects.get(tech_name=category_name)
        except Category.DoesNotExist:
            return

        return Product.objects.filter(category_id=category.id).order_by('publish_dt')


def index(request, *args, **kwargs):
    return render(request, 'base.html')


def single_product(request, ali_id):
    try:
        Product.objects.get(ali_id=ali_id)
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'base.html')


def category_products(request, category_name):
    try:
        Category.objects.get(tech_name=category_name)
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'base.html')


def product_redirect(request, ali_id):
    try:
        product = Product.objects.get(ali_id=ali_id)
    except Product.DoesNotExist:
        raise Http404
    return redirect(product.url)
