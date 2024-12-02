from django.test import TestCase
from core.models import Speaker


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://abre.ai/hopper-pic',
            website='https://abre.ai/hopper-site',
            description='Programadora e almirante.'
        )

    def test_create(self):
        self.assertTrue(Speaker.objects.exists())

    def test_description_can_be_blank(self):
        field = Speaker._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_website_can_be_blank(self):
        field = Speaker._meta.get_field('website')
        self.assertTrue(field.blank)

    def test_str(self):
        self.assertEqual('Grace Hopper', str(self.speaker))
