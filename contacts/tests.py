from django.test import TestCase
from contacts.forms import ContatcForm
from django.core import mail

class ContactTest(TestCase):
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
        self.assertContains(self.response, '<form')
        self.assertContains(self.response,'<input', 5)
        self.assertContains(self.response,'type="text"', 2)
        self.assertContains(self.response,'type="email"')
        self.assertContains(self.response,'<textarea')
        self.assertContains(self.response,'type="submit"')
    
    def test_form_has_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'phone', 'email', 'message'], list(form.fields))

class ContactPostTest(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca", phone="53-91234-5678", email="profcleberfonseca@gmail.com", message="Olá essa é a minha dúvida")
        self.response = self.client.post('/contato/', data)

    def test_post(self):
        self.assertEqual(302, self.response.status_code)
    
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
    
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Contato'
        self.assertEqual(expect, email.subject)
    
    def test_subscription_email_from(self):
        email = mail.outbox[0]
        expect = 'profcleberfonseca@gmail.com'
        self.assertEqual(expect, email.from_email)
    
    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, email.to)
    
    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Cleber Fonseca', email.body)
        self.assertIn('53-91234-5678', email.body)
        self.assertIn('profcleberfonseca@gmail.com', email.body)
        self.assertIn('Olá essa é a minha dúvida', email.body)
        
class ContactInvalidPost(TestCase):
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