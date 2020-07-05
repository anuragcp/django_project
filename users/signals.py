from django.db.models.signals import post_save
from django.contrib.auth.models import User     # here user model act as a sender
# and the receiver of the signal is a function that performs some tasks
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
