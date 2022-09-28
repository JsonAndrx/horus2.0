from datetime import datetime
import uuid
from django.db import models
from django.utils import timezone
# Create your models here.


class sendEmail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=50, blank=False)
    ip = models.CharField(max_length=50, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=59, blank=True)
    ciudad = models.CharField(max_length=50, blank=True)
    cp = models.CharField(max_length=50, blank=True)
    latitud = models.CharField(max_length=50, blank=True)
    longitud = models.CharField(max_length=50, blank=True)
    proveedor = models.CharField(max_length=50, blank=True)
    useragent = models.CharField(max_length=150, blank=True)
    completo = models.BooleanField(default=False)
    espera_completo = models.DateTimeField(blank=True, null=True)
    fecha_espera = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name = "Email"

    def __str__(self):
        return self.email

    
    def save(self):
        if self.completo:
            self.espera_completo = datetime.now()
        super(sendEmail, self).save()