from django.test import TestCase
from .models import Market

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):


    def setUp(self):
        self.market_name = 'Mom and Pop Market'
        self.market = Market(name=self.market_name)


    def test_model_can_create_market(self):
        old_count = Market.objects.count()
        self.market.save()
        new_count = Market.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.market_data = {'name': 'Grandma Louisa Whiskey Cakes'}
        self.response = self.client.post(
            reverse('create'),
            self.market_data,
            format='json'
        )

    def test_api_can_create_a_market(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_market(self):
        market = Market.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': market.id},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, market)


    def test_api_can_update_a_market(self):
        change_market = {'name': 'Grandpa Louis Pecan Pies'}
        response = self.client.put(
            reverse('details', kwargs={'pk': market.id}),
            change_market,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_market(self):
        market = Market.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': market.id}),
            format='json',
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
