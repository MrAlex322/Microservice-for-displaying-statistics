from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Statistics

class StatisticsListViewTest(TestCase):
    def test_get_context_data(self):
        # Создаем тестовые объекты Statistics
        date1 = timezone.now().date()
        date2 = date1 - timedelta(days=1)
        statistics1 = Statistics.objects.create(date=date1, views=10, clicks=5)
        statistics2 = Statistics.objects.create(date=date2, views=15, clicks=8)

        # Создаем GET-запрос к представлению
        url = reverse('statistics-list')
        response = self.client.get(url)

        # Проверяем контекст представления
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statistics_list.html')

        expected_statistics_count = 2
        self.assertEqual(len(response.context['statistics']), expected_statistics_count)

    def test_post(self):
        # Создаем POST-запрос к представлению
        url = reverse('statistics-list')
        data = {'date': '2023-07-17', 'views': 10, 'clicks': 5}
        response = self.client.post(url, data)

        # Проверяем редирект
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('statistics-list'))

        # Проверяем создание новой записи Statistics
        statistics = Statistics.objects.last()
        self.assertEqual(statistics.date, timezone.datetime.strptime('2023-07-17', '%Y-%m-%d').date())
        self.assertEqual(statistics.views, 10)
        self.assertEqual(statistics.clicks, 5)

    def test_delete_all_statistics(self):
        # Создаем тестовые объекты Statistics
        date1 = timezone.now().date()
        date2 = date1 - timedelta(days=1)
        statistics1 = Statistics.objects.create(date=date1, views=10, clicks=5)
        statistics2 = Statistics.objects.create(date=date2, views=15, clicks=8)

        # Проверяем удаление всех записей Statistics
        self.assertFalse(Statistics.objects.exists())

