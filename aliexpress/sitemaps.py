from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from aliexpress.models import Product, Category


class ProductsSitemap(Sitemap):
    changefreq = 'never'
    protocol = 'https'

    def items(self):
        return Product.objects.filter(is_published=True).order_by('publish_dt')

    def lastmod(self, obj):
        return obj.publish_dt

    def location(self, obj):
        return reverse('single_product', kwargs={'ali_id': obj.ali_id})


class CategorySitemap(Sitemap):
    changefreq = 'hourly'
    protocol = 'https'

    def items(self):
        return Category.objects.all().order_by('tech_name')

    def location(self, obj):
        return reverse('category_products', kwargs={'category_name': obj.tech_name})
