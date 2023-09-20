from django.test import TestCase

from contacts.forms import ContatcForm

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContatcForm()

    def test_form_has_fields(self):
        self.assertSequenceEqual(['name', 'phone', 'email', 'message'], list(self.form.fields))