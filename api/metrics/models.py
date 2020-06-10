from django.db import models
from django.contrib import admin
from django.contrib.postgres.fields import JSONField


class DeputadoMetrics(models.Model):
    external_id = models.IntegerField(primary_key=True, null=False, blank=False, unique=True, editable=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    metrics = JSONField()

    def __str__(self):
        return 'DeputadoMetrics(id:{})'.format(self.external_id)


admin.site.register(DeputadoMetrics)
