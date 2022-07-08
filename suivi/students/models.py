
from django.db import models
from PIL import Image
from model_utils import FieldTracker

from three_six.models import PracticalLife, SensoryMaterial, Math, Langage, Letter

from ambiance.models import Ambiance


class Students(models.Model):

    photo = models.ImageField(null=True, blank=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    profil = models.TextField()
    ambiance = models.ForeignKey(Ambiance, on_delete=models.CASCADE)
    pratique_life = models.ForeignKey(PracticalLife, on_delete=models.CASCADE)
    sensorial_material = models.ForeignKey(SensoryMaterial, on_delete=models.CASCADE)
    mathe = models.ForeignKey(Math, on_delete=models.CASCADE)
    langage = models.ForeignKey(Langage, on_delete=models.CASCADE)
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    tracker = FieldTracker()

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    IMAGE_MAX_SIZE = (100, 100)

    def resize_image(self):
        image = Image.open(self.photo)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.photo.path)

    def deactivate(self):
        self.active = False
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
