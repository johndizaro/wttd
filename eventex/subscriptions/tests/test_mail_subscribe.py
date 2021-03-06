from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Henrique Bastos', cpf=12345678901,
                    email='henrique@bastos.net', phone='41-3269-1155')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmaçao de inscriçao'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'henrique@bastos.net']
        self.assertEqual(expect, self.email.to)

    def test_subscrition_email_body(self):
        contents = ['Henrique Bastos',
                    '12345678901',
                    'henrique@bastos.net',
                    '41-3269-1155'
        ]
        for content in contents:
            self.assertIn(content, self.email.body)
