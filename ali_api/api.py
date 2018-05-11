from django.conf import settings
import requests


EPN_BASE_URL = 'http://api.epn.bz/json'


class EpnApi:
    def __init__(self, api_key=None, deeplink_hash=None, api_version=2):
        if not api_key:
            api_key = settings.EPN_API_KEY
        self.api_key = api_key

        if not deeplink_hash:
            deeplink_hash = settings.EPN_DEEPLINK_HASH
        self.deeplink_has = deeplink_hash

        self.api_version = api_version

    @staticmethod
    def _format_requests(reqs):
        data = dict()
        if isinstance(reqs, (list, tuple, set)):
            for num, req in enumerate(reqs):
                data['req{}'.format(num)] = req
        else:
            data['req0'] = reqs

        return data

    def request(self, reqs):
        params = {
            'user_api_key': self.api_key,
            'user_hash': self.deeplink_has,
            'api_version': self.api_version,
        }

        reqs = self._format_requests(reqs)
        params['requests'] = reqs
        res = requests.post(EPN_BASE_URL, json=params).json()
        if res['identified_as'] == settings.EPN_USERNAME and 'error' not in res:
            return res['results']
        # TODO: send telegram notification

    def get_products(self, offset=None, limit=100):
        req = {
            'action': 'search',
            'orderby': 'orders_count',
            'limit': limit,
        }

        if offset:
            req['offset'] = offset

        res = self.request(req)
        data = res['req0']

        if data['total_found'] < limit:
            pass  # TODO: send notification that end is probably reached

        return data['offers']

    def get_top_monthly_products(self, orderby='sales', category=None, lang=None, currency=None):
        if orderby not in ['sales', 'comission']:
            raise Exception('Wrong orderby field')

        req = {
            'action': 'top_monthly',
            'orderby': orderby,
        }

        if category:
            req['category'] = category

        if lang:
            req['lang'] = lang

        if currency:
            req['currency'] = currency

        res = self.request(req)
        return res['req0']['offers']

    def get_categories(self):
        req = {
            'action': 'list_categories'
        }
        res = self.request(req)
        return res['req0']['categories']

    def get_offer_info(self, offer_id, lang=None, currency=None):
        req = {
            'action': 'offer_info',
            'id': offer_id,
        }
        if lang:
            req['lang'] = lang

        if currency:
            req['currency'] = currency

        res = self.request(req)
        return res['req0']
