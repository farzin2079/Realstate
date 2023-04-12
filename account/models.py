from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    realstate = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(
        upload_to="photo/account/%Y/%m/%d/",
        default="defaults/default.jpg",
        null=True,
        blank=True,
    )
    telephone = models.CharField(max_length=50, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=1000, null=True, blank=True)
    whatsapp = models.CharField(max_length=50, null=True, blank=True)
    propertys = models.ManyToManyField(
        "property.Property", related_name="propertys"
    )
    watchlist = models.ManyToManyField(
        "property.Property", related_name="property_watch"
    )
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.username
