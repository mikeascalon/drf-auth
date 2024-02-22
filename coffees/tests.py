from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Coffee

class CoffeeTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = get_user_model().objects.create_user(username="testuser1", password="pass")
        testuser1.save()

        # Create a coffee instance
        test_coffee = Coffee.objects.create(
            owner=testuser1,
            name="Espresso",
            description="A full-flavored, concentrated form of coffee.",
            price=2.99
        )
        test_coffee.save()

    def setUp(self):
        # Log in the user for each test
        self.client.login(username="testuser1", password="pass")

    def test_coffees_model(self):
        coffee = Coffee.objects.get(id=1)
        actual_owner = str(coffee.owner)
        actual_name = str(coffee.name)
        actual_description = str(coffee.description)
        actual_price = coffee.price
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Espresso")
        self.assertEqual(actual_description, "A full-flavored, concentrated form of coffee.")
        self.assertEqual(actual_price, 2.99)

    def test_get_coffee_list(self):
        url = reverse("coffee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        coffees = response.data
        self.assertEqual(len(coffees), 1)
        self.assertEqual(coffees[0]["name"], "Espresso")

    def test_get_coffee_by_id(self):
        url = reverse("coffee_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        coffee = response.data
        self.assertEqual(coffee["name"], "Espresso")

    def test_create_coffee(self):
        url = reverse("coffee_list")
        data = {
            "owner": 1,
            "name": "Latte",
            "description": "Espresso mixed with steamed milk",
            "price": "3.50"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        coffees = Coffee.objects.all()
        self.assertEqual(len(coffees), 2)
        self.assertEqual(Coffee.objects.get(id=2).name, "Latte")

    def test_update_coffee(self):
        url = reverse("coffee_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Espresso",
            "description": "Short and strong coffee with a rich flavor",
            "price": "2.99"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        coffee = Coffee.objects.get(id=1)
        self.assertEqual(coffee.name, data["name"])
        self.assertEqual(coffee.owner.id, data["owner"])
        self.assertEqual(coffee.description, data["description"])
        self.assertEqual(str(coffee.price), data["price"])

    def test_delete_coffee(self):
        url = reverse("coffee_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        coffees = Coffee.objects.all()
        self.assertEqual(len(coffees), 0)

    def test_authentication_required(self):
        self.client.logout()
        url = reverse("coffee_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
