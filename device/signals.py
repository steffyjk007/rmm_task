# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Device
#
# @receiver(post_save, sender=Device)
# def device_update_notification(sender, instance, created, **kwargs):
#     if created:
#         print(f"New Device created: {instance.device_name}")
#     else:
#         print(f"Device updated: {instance.device_name}")

from asgiref.sync import async_to_sync
import json
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Device


@receiver(post_save, sender=Device)
def device_update_notification(sender, instance, created, **kwargs):
    if created:
        message = f"New Device created: {instance.device_name}"
    else:
        message = f"Device updated: {instance.device_name}"

    # Send the message to the WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'device_updates',
        {
            'type': 'device_update_notification',
            'message': message
        }
    )
