from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Statistics


class StatisticsListViewTest(TestCase):

    def test_post_create(self):
        url = reverse('statistics-list')
        data = {
            'date': '2023-07-17',
            'views': 200,
            'clicks': 40,
            'create': '',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(Statistics.objects.filter(date='2023-07-17', views=200, clicks=40).exists())

    def test_post_delete(self):
        url = reverse('statistics-list')
        data = {'delete': ''}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

        self.assertFalse(Statistics.objects.exists())


class StatisticsModelTest(TestCase):
    def test_save_method(self):
        statistics = Statistics(date='2023-07-18', views=100, clicks=20)

        statistics.save()

        self.assertEqual(statistics.cost, 10.0)
        self.assertEqual(statistics.cpc, 0.5)
        self.assertEqual(statistics.cpm, 100.0)


    def test_save_method_with_zero_views(self):
        statistics = Statistics(date='2023-07-18', views=0, clicks=20)

        statistics.save()

        self.assertEqual(statistics.cost, 10.0)
        self.assertEqual(statistics.cpc, 0.5)
        self.assertIsNone(statistics.cpm)