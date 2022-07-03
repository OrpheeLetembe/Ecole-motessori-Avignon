from django.db import models

from django.contrib.auth.models import AbstractUser

from ambiance.models import Ambiance


class User(AbstractUser):
    CHOICES = (
        ('educator', 'Educatrice'),
        ('assistant', 'Assistante')
    )

    ambiance = models.ForeignKey(Ambiance, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=100, choices=CHOICES, verbose_name="Role")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
