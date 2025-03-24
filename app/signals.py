from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Event
import os
from django.conf import settings

@receiver(post_delete, sender=Event)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        image_path = os.path.join(settings.MEDIA_ROOT, instance.image.path)
        if os.path.isfile(image_path):
            os.remove(image_path)