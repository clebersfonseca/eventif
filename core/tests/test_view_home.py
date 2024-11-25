from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        '''
        Testa se a página inicial retorna status code 200
        '''
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_link_subscription(self):
        self.assertContains(
            self.response, 'href="{}"'.format(r('subscriptions:new')))
