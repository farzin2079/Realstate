from django.db.models.signals import post_save, post_delete
import os
from django.core.files.storage import default_storage
from django.db.models import FileField
from django.db import models
from django.db.models.signals import post_delete

from django.contrib.auth.models import User
from .models import Profile


def createprofile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


def deleteuser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createprofile, sender=User)
post_delete.connect(deleteuser, sender=Profile)
