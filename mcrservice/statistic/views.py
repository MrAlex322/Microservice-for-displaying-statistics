from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Statistics
from .serializer import StatisticsSerializer


class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        statistics = Statistics.objects.order_by('date')
        serializer = self.get_serializer(statistics, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def filter_by_date(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        queryset = self.get_queryset()
        if start_date:
            queryset = queryset.filter(date__gte=start_date)
        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        Statistics.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



