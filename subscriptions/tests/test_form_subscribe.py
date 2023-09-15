from django.test import TestCase

from subscriptions.forms import SubscriptionForm


class subscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_form_has_fields(self):
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields)) 