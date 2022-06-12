from django.db import models

from PIL import Image


class Students(models.Model):
    BOIS = 'BOIS'
    TERRE = 'TERRE'

    ENVIRONMENT_CHOICES = (
        (BOIS, 'Bois'),
        (TERRE, 'Terre'),

    )
    image = models.ImageField(null=True, blank=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    ambiance = models.CharField(max_length=100, choices=ENVIRONMENT_CHOICES)
    reference_email = models.CharField(max_length=100)
    reference_phone = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

