from django.apps import AppConfig


class MetricsConfig(AppConfig):
    name = 'metrics'

    def ready(self):
        import metrics.signals
