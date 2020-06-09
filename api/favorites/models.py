from django.db import models

from user.models import CustomUser


class FavoriteProposicao(models.Model):
    proposicao_id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    year = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    
    
class FavoriteDeputado(models.Model):
    deputado_id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    partido = models.CharField(max_length=10, blank=False, null=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
