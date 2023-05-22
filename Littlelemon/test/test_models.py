from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(title="cow milk", price=10, inventory=100)

    def test_fields(self):
        self.assertIsInstance(self.menu.title, str)
        self.assertIsInstance(self.menu.price, int)

    def test_created_item(self):
        self.assertEqual(self.menu.title, 'cow milk')

    