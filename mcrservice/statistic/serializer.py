from rest_framework import serializers

from .models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'

    def validate_views(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise serializers.ValidationError("Значение 'views' должно быть неотрицательным целым числом.")
        return value if value is not None else 0

    def validate_clicks(self, value):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise serializers.ValidationError("Значение 'clicks' должно быть неотрицательным целым числом.")
        return value if value is not None else 0
