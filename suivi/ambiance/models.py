from django.db import models


class Ambiance(models.Model):
    BOIS = 'BOIS'
    TERRE = 'TERRE'

    ENVIRONMENT_CHOICES = (
        (BOIS, 'Bois'),
        (TERRE, 'Terre'),

    )
    name = models.CharField(max_length=100, choices=ENVIRONMENT_CHOICES)
    year = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.year}'
