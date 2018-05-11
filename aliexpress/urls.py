from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import url, include
from django.urls import path
from django.contrib.sitemaps import views as sitemap_views

from aliexpress import views, sitemaps as ali_sitemaps

sitemaps = {
    'products': ali_sitemaps.ProductsSitemap,
    'category': ali_sitemaps.CategorySitemap,
}

api_urlpatterns = [
    url(r'^products/$', views.ProductsList.as_view()),
    url(r'^products/(?P<category_name>[\w]+)$', views.ProductsList.as_view()),
    url(r'^product/(?P<ali_id>[0-9]+)$', views.ProductDetail.as_view()),
    url(r'^categories/$', views.CategoriesList.as_view()),
    url(r'^category_products/(?P<category_name>[\w]+)$', views.FilterByCategory.as_view()),
]

urlpatterns = [
    url(r'^api/', include(api_urlpatterns)),
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<ali_id>[\d]+)$', views.single_product, name='single_product'),
    url(r'^c/(?P<category_name>[\w]+)$', views.category_products, name='category_products'),
    url(r'^redirect/(?P<ali_id>[\d]+)$', views.product_redirect),

    path('sitemap.xml', sitemap_views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', sitemap_views.sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

urlpatterns = format_suffix_patterns(urlpatterns)
