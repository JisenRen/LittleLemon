import json
from django.test import TestCase
from django.urls import reverse
from restaurant.models import *
from restaurant.serializers import *


# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title='Alice', price='6.50', inventory=38)
        Menu.objects.create(title='Bob', price='3.99', inventory=64)
        Menu.objects.create(title='Carol', price='7.50', inventory=73)

    def test_get_all(self):
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)
        serialized_data = json.loads(json.dumps(serialized.data))

        response = self.client.get(reverse('api_menu'))
        response_data = json.loads(str(response.content, 'UTF-8'))

        self.assertEqual(serialized_data, response_data)
