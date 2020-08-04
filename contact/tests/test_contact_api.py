from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Contact
from contact.serializers import ContactSerializer

CONTACTS_URL = reverse('contact:contact-list')

class PublicContactsApiTests(TestCase):
    """tests for public contacts api"""

    def setUp(self):
        self.client = APIClient()

    def test_post_new_contact(self):
        """test that we can send in a new contact"""
        payload = {
            'name': 'Mr. Mittens',
            'email': 'mittens@meow.com',
            'comments': 'please clean my litter box, you slave',
        }

        self.client.post(CONTACTS_URL, payload)

        exists = Contact.objects.filter(
            name = payload['name']
        ).exists()

        self.assertTrue(exists)

    def test_get_method_not_allowed(self):
        """test that the get method is not allowed"""

        response = self.client.get(CONTACTS_URL)
    
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
