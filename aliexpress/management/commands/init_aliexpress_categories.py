from django.core.management.base import BaseCommand
from django.db import IntegrityError

from ali_api.api import EpnApi
from aliexpress.models import Category


class Command(BaseCommand):
    help = 'Initializes aliexpress product categories'

    def handle(self, *args, **options):
        api = EpnApi()
        categories = api.get_categories()

        # workaround for some products with category_id == 0
        categories.append({
            'id': 0,
            'title': 'Other',
        })
        total = len(categories)
        created_count = 0
        for cat in categories:
            category_id = cat['id']
            category_name = cat['title'].replace('&', 'and')
            category_tech_name = category_name.replace('\'', '').replace(' ', '_').lower()
            try:
                category, created = Category.objects.update_or_create(
                    category_id=category_id,
                    defaults={
                        'name': category_name,
                        'tech_name': category_tech_name
                    }
                )
                if created:
                    created_count += 1
            except IntegrityError:
                self.stdout.write(f'Category already exists: id={category_id}, name={category_name}')

        self.stdout.write(f'Got {total} categories.\n{created_count} created')
