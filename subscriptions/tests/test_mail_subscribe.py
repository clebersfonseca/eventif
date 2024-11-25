from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca", cpf='12345678901',
                    email='profcleberfonseca@gmail.com', phone='53-12345-6789')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição!'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Cleber Fonseca',
            '12345678901',
            'profcleberfonseca@gmail.com',
            '53-12345-6789'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
