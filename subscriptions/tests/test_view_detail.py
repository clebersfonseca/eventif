from django.test import TestCase
from subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        obj = Subscription.objects.create(
            name='Cleber Fonseca',
            cpf='12345678901',
            email='profcleberfonseca@gmail.com',
            phone='53-91234-5678'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = ('Cleber Fonseca', '12345678901',
                    'profcleberfonseca@gmail.com', '53-91234-5678')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(resp.status_code, 404)
