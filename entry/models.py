from django.db import models
from django.contrib.auth.models import User


class Door(models.Model):
    name = models.CharField(
        'Door Name',
        max_length=64,
        blank=False,
        null=False
    )
    ip = models.CharField(
        'IP Address',
        max_length=16,
        blank=False,
        null=False
    )
    port = models.IntegerField(
        'Port',
        null=False
    )
    status = models.CharField(
        'Last Known Status',
        max_length=64,
        blank=False,
        null=False
    )


class Key(models.Model):
    door = models.ForeignKey(
        Door,
        name="Door",
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        name="User",
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    recycle = models.BooleanField(
        'Recycle After Use',
        default=True,
        blank=False,
        null=False
    )
