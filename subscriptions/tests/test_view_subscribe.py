from django.test import TestCase
from django.core import mail
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscribeGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1)
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca", cpf='12345678901',
                    email='profcleberfonseca@gmail.com', phone='53-12345-6789')
        self.resp = self.client.post(r('subscriptions:new'), data)

    def test_post(self):
        self.assertRedirects(self.resp, r('subscriptions:detail', 1))

    def test_send_subscription_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())
