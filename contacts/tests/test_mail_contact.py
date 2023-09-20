from django.test import TestCase
from django.core import mail

class MailTest(TestCase):
    def setUp(self):
        data = dict(
            name="Cleber Fonseca", 
            phone="53-91234-5678", 
            email="profcleberfonseca@gmail.com", 
            message="Olá essa é a minha dúvida")
        self.response = self.client.post('/contato/', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Contato'
        self.assertEqual(expect, self.email.subject)
    
    def test_contact_email_from(self):
        expect = 'profcleberfonseca@gmail.com'
        self.assertEqual(expect, self.email.from_email)
    
    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, self.email.to)
    
    def test_contact_email_body(self):
        contents = ['Cleber Fonseca',
                    '53-91234-5678',
                    'profcleberfonseca@gmail.com',
                    'Olá essa é a minha dúvida']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)