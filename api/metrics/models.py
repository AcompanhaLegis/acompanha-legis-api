from django.db import models
from django.contrib.postgres.fields import JSONField


class DeputadoMetrics(models.Model):
    external_id = models.IntegerField(null=False, blank=False, unique=True)
    metrics = JSONField()

    def __str__(self):
        return 'DeputadoMetrics(id:{})'.format(self.external_id)
