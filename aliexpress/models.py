from django.db import models
from django.utils import timezone as tz


class Category(models.Model):
    category_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=60)
    tech_name = models.CharField(max_length=60)


class Store(models.Model):
    store_id = models.IntegerField()
    title = models.CharField(max_length=50, default='')


class Product(models.Model):
    USD = 1
    RUB = 2
    CURRENCIES = (
        (USD, 'usd'),
        (RUB, 'rub')
    )

    ali_id = models.BigIntegerField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.TextField()
    description = models.TextField()
    preview_url = models.URLField()
    currency = models.IntegerField(choices=CURRENCIES)
    price = models.FloatField()
    url = models.URLField()
    short_url = models.URLField()
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)
    added_dt = models.DateTimeField(default=tz.now)
    is_published = models.BooleanField(default=False)
    publish_dt = models.DateTimeField(null=True, blank=True)


class Picture(models.Model):
    product = models.ForeignKey(Product, related_name='pictures', on_delete=models.CASCADE)
    url = models.URLField()
