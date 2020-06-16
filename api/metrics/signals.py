from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from metrics.models import DeputadoMetrics

from updates.models import UpdateSubscription


@receiver(post_save, sender=DeputadoMetrics)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    subscribers = UpdateSubscription.objects.filter(
        external_model='D',
        external_id=instance.external_id
    )

    name = subscribers[0].name
    deputado_id = subscribers[0].external_id
    emails = list(subscribers.values_list('user__email', flat=True))

    with mail.get_connection() as conn:
        html_content = '<div style="text-align: center;"><h2 style="color: #1890FF;">Acompanha legis - Atualização</h2><br/><p>Acabamos de receber uma atualização para {}!</p><br/><a href="https://acompanhalegis.com.br/deputados/{}">Confira agora!</a></div>'.format(
            name, deputado_id)
        email = mail.EmailMultiAlternatives(
            'Atualização [Deputado]',
            'Atualização recebida para {}'.format(name),
            'noreply@acompanhalegis.com.br',
            emails,
            [],
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
