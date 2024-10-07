from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from trading.models import Supplier


# Create your tests here.


class SupplierTestCase(APITestCase):
    """Test Supplier API."""

    def setUp(self):
        self.user = User.objects.create(username="test@example.com")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.supplier = Supplier.objects.create(
            user=self.user,
            title="factory",
            email="factory@example.com",
            country="USA",
            city="Dallas",
            street="Plaza st.",
            house="525",
            level="factory",
        )

    def test_supplier_create(self):
        """Testing adding a supplier."""

        url = reverse("trading:suppliers-list")
        data = {
            "title": "retail 1",
            "email": "retail@example.com",
            "country": "USA",
            "city": "Houston",
            "street": "Bankside dr.",
            "house": "5603",
            "level": "retail",
            "vendor": self.supplier.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 2)
        self.assertEqual(response.json()['house'], '5603')

    def test_supplier_list(self):
        """Testing getting a list of suppliers."""

        url = reverse("trading:suppliers-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.all().count(), 1)

    def test_supplier_retrieve(self):
        """Testing getting a supplier."""

        url = reverse("trading:suppliers-detail", kwargs={'pk': self.supplier.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['country'], 'USA')

    def test_supplier_update(self):
        """Testing a partial supplier update."""
        data = {
            "title": "factory new",
        }
        url = reverse("trading:suppliers-detail", kwargs={'pk': self.supplier.id})
        response = self.client.patch(url, data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'factory new')

    def test_supplier_delete(self):
        """Supplier removal testing."""
        url = f'{reverse("trading:suppliers-list")}{self.supplier.pk}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.all().count(), 0)
