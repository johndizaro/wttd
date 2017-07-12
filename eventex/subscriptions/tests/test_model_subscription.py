from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscritionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='John Evan Dizaro',
            cpf='12345678901',
            email='johndizaro@gmail.com',
            phone='41-995404240'
        )
        self.obj.save()

    def test_create(self):

        self.assertTrue(Subscription.objects.exists())

    def test_cresate_at(self):
        """Subscription must have an auto create_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)