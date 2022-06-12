from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BOIS = 'BOIS'
    TERRE = 'TERRE'

    ENVIRONMENT_CHOICES = (
        (BOIS, 'Bois'),
        (TERRE, 'Terre'),

    )
    phone = models.CharField(max_length=100)
    ambiance = models.CharField(max_length=100, choices=ENVIRONMENT_CHOICES)
