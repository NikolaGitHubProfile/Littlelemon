from django.test import TestCase, RequestFactory
from restaurant.views import MenuItemView
from restaurant.models import Menu
from django.shortcuts import render
from restaurant.serializers import MenuSerializer
from rest_framework.response import Response

class MenuViewTest(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()
        Menu.objects.create(title="cow milk", price=10, inventory=100)
        Menu.objects.create(title="cheese", price=50, inventory=100)

    def test_getall(self):
        queryset = Menu.objects.all()
        serializer = MenuSerializer(queryset, many=True)
        
        request = self.factory.get(path='restaurant/menu/')
        response = MenuItemView.as_view()(request)

        self.assertEqual(serializer.data, response.data)
        
        





