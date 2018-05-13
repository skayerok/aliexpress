from datetime import timedelta

broker_url = 'amqp://guest:guest@localhost:5672//'

imports = ('aliexpress.tasks', )

beat_schedule = {
    'aliexpress.publish_product': {
        'task': 'aliexpress.publish_product',
        'schedule': timedelta(hours=1)
    },
}

try:
    from .celeryconfig_local import *
except ImportError:
    pass
