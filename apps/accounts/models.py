from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.username


class AbstractOwned(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        # related_name="owner",
    )
    # owner_group = models.ForeignKey("auth.Group", null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
