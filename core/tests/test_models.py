from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """test suite covering model functionality"""

    def test_create_contact(self):
        """test that we can create a contact"""
        contact = models.Contact.objects.create(
            name="Prof. Meow Meow",
            email="me@www.meow",
            comments="Meow?",
        )

        self.assertEqual(contact.name, "Prof. Meow Meow")

    def test_create_contact_blank_fields(self):
        """test that we can leave the comments and name fields blank"""
        contact = models.Contact.objects.create(
            name="",
            email="me@ww.meow",
            comments = "",
        )

        self.assertEqual(contact.email, "me@ww.meow")