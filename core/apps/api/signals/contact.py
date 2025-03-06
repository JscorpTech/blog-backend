from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import ContactModel


@receiver(post_save, sender=ContactModel)
def ContactSignal(sender, instance, created, **kwargs):
    if created:
        print("ContactSignal created: {}".format(instance.title))
