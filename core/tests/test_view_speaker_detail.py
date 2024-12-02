from django.test import TestCase
from django.shortcuts import resolve_url as r

from core.models import Speaker


class SpeakerDetailGet(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://abre.ai/hopper-pic',
            website='https://abre.ai/hopper-site',
            description='Programadora e almirante.'
        )
        self.resp = self.client.get(r('speaker_detail', slug=speaker.slug))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante',
            'https://abre.ai/hopper-pic',
            'https://abre.ai/hopper-site'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, resp.status_code)
