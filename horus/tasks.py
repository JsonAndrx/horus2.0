from celery import shared_task
from .models import sendEmail
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import sendEmail
from django.conf import settings

@shared_task(blind=True)
def delete_register():
    limite = datetime.now() - timedelta(seconds=120)
    files = sendEmail.objects.filter(espera_completo__lte=limite)
    if files:
        files.delete()
        return "registros eliminados"
    return "no hay registros expirados"

@shared_task(blind=True)
def delete_register_expired():
    limite = datetime.now() - timedelta(seconds=120)
    files = sendEmail.objects.filter(fecha_espera__lte=limite)
    if files:
        files.delete()
        return "archivos eliminados"
    return "no hay archivos expirados"



