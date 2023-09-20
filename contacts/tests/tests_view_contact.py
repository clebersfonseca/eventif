from django.test import TestCase
from contacts.forms import ContatcForm
from django.core import mail

class ContactGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/contato/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contacts/contact_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ContatcForm)
    
    def test_html(self):
        tags = (("<form", 1),
                ("<input", 5),
                ('type="text"', 2),
                ('type="email"', 1),
                ('<textarea', 1),
                ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)    
    

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca", phone="53-91234-5678", email="profcleberfonseca@gmail.com", message="Olá essa é a minha dúvida")
        self.response = self.client.post('/contato/', data)

    def test_post(self):
        self.assertEqual(302, self.response.status_code)
    
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
    
    
        
class ContactPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contacts/contact_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ContatcForm)

    def test_form_has_error(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class ContactSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name = "Cleber Fonseca", phone = '53-91234-5678',
                    email = 'profcleberfonseca@gmail.com', message='Olá essa é a minha dúvida')
        response = self.client.post('/contato/', data, follow=True)
        self.assertContains(response, 'Contato enviado com sucesso!')