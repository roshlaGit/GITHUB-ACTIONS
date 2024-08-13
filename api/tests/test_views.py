# appname/tests/test_views.py

from django.urls import reverse
from rest_framework.test import APITestCase

class GetItemsTest(APITestCase):
    def test_get_items(self):
        url = reverse('get_items')
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.data['items'] == ["Item 1", "Item 2", "Item 3"]
