from django.test import TestCase
from core.models import Speaker, ContactSpeaker
from django.core.exceptions import ValidationError


class ContactSpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name="Cleber Fonseca",
            slug="cleber-fonseca",
            photo="https://cleberfonseca.com.br/img/perfil.png"
        )

    def test_email(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
            kind=ContactSpeaker.EMAIL,
            value='profcleberfonseca@gmail.com'
        )
        self.assertTrue(ContactSpeaker.objects.exists())

    def test_phone(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
            kind=ContactSpeaker.PHONE,
            value='53-912345678'
        )
        self.assertTrue(ContactSpeaker.objects.exists())

    def test_choices(self):
        contact = ContactSpeaker.objects.create(
            speaker=self.speaker,
            kind='A',
            value='B'
        )
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = ContactSpeaker(
            speaker=self.speaker,
            kind=ContactSpeaker.EMAIL,
            value='profcleberfonseca@gmail.com'
        )
        self.assertEqual('profcleberfonseca@gmail.com', str(contact))
