from django.db import models
from django.contrib.auth.models import User

from account.models import Profile


# Create your models here.
class Property(models.Model):
    real_state = models.ForeignKey(
        Profile, related_name="real_state", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    vpm = models.IntegerField(null=True, blank=True)
    value = models.IntegerField(null=True, blank=True)
    image1 = models.ImageField(
        upload_to="photo/property/%Y/%m/%d/",
        default="defaults/default.jpg",
        null=True,
        blank=True,
    )
    image2 = models.ImageField(
        upload_to="photo/property/%Y/%m/%d/",
        default="defaults/default.jpg",
        null=True,
        blank=True,
    )
    image3 = models.ImageField(
        upload_to="photo/property/%Y/%m/%d/",
        default="defaults/default.jpg",
        null=True,
        blank=True,
    )
    image4 = models.ImageField(
        upload_to="photo/property/%Y/%m/%d/",
        default="defaults/default.jpg",
        null=True,
        blank=True,
    )
    category = models.ForeignKey("Category", related_name="category", on_delete=models.PROTECT, null=True, blank=True)
    watchlist = models.ManyToManyField(
        "account.Profile", related_name="Profile_watch", null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    property = models.ManyToManyField(Property, related_name="property_category", null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name