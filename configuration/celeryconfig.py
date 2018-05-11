from datetime import timedelta

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_IMPORTS = ('aliexpress.tasks', )

CELERYBEAT_SCHEDULE = {
    'aliexpress.publish_product': {
        'task': 'aliexpress.publish_product',
        'schedule': timedelta(hours=1)
    },
}
