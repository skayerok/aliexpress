from celery.task import task

from django.utils import timezone as tz

from ali_api.api import EpnApi
from configuration.celery import app
from aliexpress.models import Product, Store, Picture, Category

# internal fieldname -> external fieldname
FIELDS_MAP = {
    'ali_id': 'id',
    # 'category_id': 'id_category',
    'name': 'name',
    'preview_url': 'picture',
    # 'all_images':,
    'price': 'price',
    # 'sale_price':,
    # 'currency': 'currency',
    'description': 'description',
    # 'store_id': 'store_id',
    # 'store_title':,
    'url': 'url',
}

CURRENCIES_MAP = {
    'usd': Product.USD,
    'rub': Product.RUB,
}


def _map_product_fields(product_data):
    new_data = {}
    for int_field, ext_field in FIELDS_MAP.items():
        new_data[int_field] = product_data.get(ext_field)

    new_data['currency'] = CURRENCIES_MAP.get(product_data['currency'].lower())

    return new_data


def _create_product(product_data):
    tidy_product_data = _map_product_fields(product_data)
    store_id = product_data['store_id']
    store_title = product_data['store_title']
    store, created = Store.objects.get_or_create(store_id=store_id)
    if created:
        store.title = store_title
        store.save()

    category = Category.objects.get(category_id=product_data['id_category'])

    product = Product.objects.create(
        **tidy_product_data,
        store=store,
        category=category,
    )

    for image_url in product_data['all_images']:
        Picture.objects.create(
            product=product,
            url=image_url
        )


def create_ali_products():
    api = EpnApi()

    offset = 0
    while True:
        external_products = api.get_products(offset=offset)
        product_ids = set([int(p['id']) for p in external_products])
        internal_product_ids = set(Product.objects.filter(ali_id__in=product_ids).values_list('ali_id', flat=True))
        absent_product_ids = product_ids - internal_product_ids
        if absent_product_ids:
            products_to_add = filter(lambda p: int(p['id']) in absent_product_ids, external_products)
            for product in products_to_add:
                _create_product(product)
            break
        else:
            offset += 100


@app.task(
    name='aliexpress.publish_product',
)
def publish_product():
    not_published_products = Product.objects.filter(is_published=False).order_by('added_dt')
    if not not_published_products.exists():
        create_ali_products()
        not_published_products = Product.objects.filter(is_published=False).order_by('added_dt')

    product = not_published_products.last()
    product.is_published = True
    product.publish_dt = tz.now()
    product.save(update_fields=('is_published', 'publish_dt'))
