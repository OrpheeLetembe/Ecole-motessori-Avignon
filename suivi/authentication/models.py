from django.db import models

from django.contrib.auth.models import AbstractUser
from ambiance.models import Ambiance


class User(AbstractUser):

    ambiance = models.ForeignKey(Ambiance, on_delete=models.CASCADE, blank=True, null=True)

