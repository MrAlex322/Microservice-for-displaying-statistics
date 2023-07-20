import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Statistics

class StatisticsViewSetTests(TestCase):
    def setUp(self):
        # Создаем тестовый объект Statistics
        self.statistics = Statistics.objects.create(date='2023-07-01', views=100, clicks=50)

    def test_create_statistics(self):
        # Проверяем создание объекта Statistics через POST запрос
        url = reverse('statistics-list')
        data = {'date': '2023-07-02', 'views': 200, 'clicks': 80}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Statistics.objects.count(), 2)

    def test_list_statistics(self):
        # Проверяем получение списка всех Statistics через GET запрос
        url = reverse('statistics-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_by_date(self):
        # Проверяем фильтрацию Statistics по дате через GET запрос с параметрами start_date и end_date
        url = reverse('statistics-filter-by-date')
        response = self.client.get(url, {'start_date': '2023-07-01', 'end_date': '2023-07-03'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delete_all_statistics(self):
        # Проверяем удаление всех Statistics через DELETE запрос
        url = reverse('statistics-delete-all')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Statistics.objects.count(), 0)