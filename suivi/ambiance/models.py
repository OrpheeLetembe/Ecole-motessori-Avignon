from django.db import models


class Ambiance(models.Model):
    ENVIRONMENT_CHOICES = (
        ('BOIS', 'Bois'),
        ('TERRE', 'Terre'),

    )
    name = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES, verbose_name="Ambiance")
    year = models.CharField(max_length=20, verbose_name="Année")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.year}'
