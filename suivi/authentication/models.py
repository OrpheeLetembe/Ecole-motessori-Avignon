from django.db import models

from django.contrib.auth.models import AbstractUser
from ambiance.models import Ambiance


class User(AbstractUser):

    ambiance = models.ForeignKey(Ambiance, null=True, blank=True, on_delete=models.CASCADE)
