from django.test import TestCase

class TestHome(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_home(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')