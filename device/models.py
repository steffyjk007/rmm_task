from django.db import models

STATUS_CHOICES = (
    ('active', 'active'),
    ('inactive', 'inactive')
)


class Device(models.Model):
    device_name = models.CharField(unique=True, max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, default='active', max_length=100)
    last_update_time = models.DateTimeField(auto_now=True)