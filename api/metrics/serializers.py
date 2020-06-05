from rest_framework import serializers

from metrics.models import DeputadoMetrics


class DeputadoMetricsSerializer(serializers.ModelSerializer):
    model = DeputadoMetrics
    fields = '__all__'
