from django.db import models

from user.models import CustomUser


class FavoriteProposicao(models.Model):
    proposicao_id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE, related_name='favorite_proposicoes')
    
    
class FavoriteDeputado(models.Model):
    deputado_id = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    partido = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE, related_name='favorite_deputados')
