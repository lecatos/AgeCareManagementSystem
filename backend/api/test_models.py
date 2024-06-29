#Core Django imports
from django.test import TestCase

#Third-party app imports
from model_bakery import baker

from client.models import Client

class CustomerTestModel(TestCase):
    """
    Class to test the model Customer
    """

    def setUp(self):
        self.customer = baker.make(Client)