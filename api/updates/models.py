from django.db import models
from django.contrib import admin

from user.models import CustomUser


class UpdateSubscription(models.Model):
    SUBSCRIPTION_CHOICES = (
        ('D', 'Deputado'),
        ('P', 'Proposicao')
    )

    external_id = models.IntegerField(null=False, blank=False)
    external_model = models.CharField(max_length=1, choices=SUBSCRIPTION_CHOICES, null=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE, related_name='subscriptions')

    class Meta:
        unique_together = ['external_id', 'user']


admin.site.register(UpdateSubscription)
