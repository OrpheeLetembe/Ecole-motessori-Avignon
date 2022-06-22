from django.db import models

from PIL import Image

from ambiance.models import Ambiance


class Students(models.Model):

    image = models.ImageField(null=True, blank=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    ambiance = models.ForeignKey(Ambiance, on_delete=models.CASCADE)
    observations_trim1 = models.TextField(null=True, blank=True)
    observations_trim2 = models.TextField(null=True, blank=True)
    observations_trim3 = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    IMAGE_MAX_SIZE = (100, 100)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

