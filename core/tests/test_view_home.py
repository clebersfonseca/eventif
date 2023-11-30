from django.test import TestCase
from django.shortcuts import resolve_url as r


class TestHome(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_home(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expect = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expect)

    def test_speakers(self):
        contents = [
            'Grace Hopper',
            'https://cleberfonseca.com.br/img/hopper.jpeg',
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'Alan Turing',
            'https://cleberfonseca.com.br/img/turing.jpeg',
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_talks_link(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)
