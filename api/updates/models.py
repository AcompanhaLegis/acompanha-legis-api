from django.db import models

from user.models import CustomUser


class UpdateSubscription(models.Model):
    SUBSCRIPTION_CHOICES = (
        ('D', 'Deputado'),
        ('P', 'Proposicao')
    )

    external_id = models.IntegerField(null=False, blank=False, unique=True)
    external_model = models.CharField(max_length=1, choices=SUBSCRIPTION_CHOICES, null=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
