from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestHome(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_home(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expect = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expect)
