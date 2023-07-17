from rest_framework import serializers

from .models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('date', 'views', 'clicks', 'cost', 'cpc', 'cpm')
