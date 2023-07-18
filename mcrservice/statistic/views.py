from datetime import datetime
from django.shortcuts import redirect
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Statistics
from .serializer import StatisticsSerializer
from django.views.generic import TemplateView
from django.contrib import messages


# Для работы с json
# class StatisticsViewSet(viewsets.ModelViewSet):
#     queryset = Statistics.objects.all()
#     serializer_class = StatisticsSerializer
#
#     def list(self, request):
#         statistics = Statistics.objects.order_by('date')
#         serializer = self.get_serializer(statistics, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['delete'])
#     def delete_all(self, request):
#         Statistics.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @action(detail=False, methods=['get'])
# def filter_by_date(self, request):
#     start_date = request.query_params.get('start_date')
#     end_date = request.query_params.get('end_date')
#
#     queryset = self.get_queryset()
#     if start_date:
#         queryset = queryset.filter(date__gte=start_date)
#     if end_date:
#         queryset = queryset.filter(date__lte=end_date)
#
#     serializer = self.get_serializer(queryset, many=True)
#     return Response(serializer.data)


class StatisticsListView(TemplateView):
    template_name = 'statistics_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        from_date = self.request.GET.get('from')
        to_date = self.request.GET.get('to')

        if from_date and to_date:
            from_date = datetime.strptime(from_date, '%Y-%m-%d')
            to_date = datetime.strptime(to_date, '%Y-%m-%d')

            statistics = Statistics.objects.filter(date__range=(from_date, to_date)).order_by('date')
        else:
            statistics = Statistics.objects.all().order_by('date')

        serializer = StatisticsSerializer(statistics, many=True)

        context['statistics'] = serializer.data

        return context

    def post(self, request, *args, **kwargs):
        if 'create' in request.POST:
            date = request.POST.get('date')
            views = int(request.POST.get('views'))
            clicks = int(request.POST.get('clicks'))

            Statistics.objects.create(date=date, views=views, clicks=clicks)

            messages.success(request, 'Запись успешно создана.')
            return self.get(request, *args, **kwargs)

        elif 'delete' in request.POST:
            Statistics.objects.all().delete()
            messages.success(request, 'Все записи успешно удалены.')
            return self.get(request, *args, **kwargs)
