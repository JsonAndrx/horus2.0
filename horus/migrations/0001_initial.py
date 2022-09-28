# Generated by Django 4.0.7 on 2022-09-27 15:31

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sendEmail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('ip', models.CharField(blank=True, max_length=50)),
                ('pais', models.CharField(blank=True, max_length=50)),
                ('estado', models.CharField(blank=True, max_length=59)),
                ('ciudad', models.CharField(blank=True, max_length=50)),
                ('cp', models.CharField(blank=True, max_length=50)),
                ('latitud', models.CharField(blank=True, max_length=50)),
                ('longitud', models.CharField(blank=True, max_length=50)),
                ('proveedor', models.CharField(blank=True, max_length=50)),
                ('useragent', models.CharField(blank=True, max_length=150)),
                ('completo', models.BooleanField(default=False)),
                ('espera_completo', models.DateTimeField(blank=True)),
                ('fecha_espera', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Email',
            },
        ),
    ]
