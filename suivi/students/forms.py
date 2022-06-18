from django import forms
from .models import Students
from ambiance.models import Ambiance


class StudentForm(forms.ModelForm):
    ENVIRONMENT_CHOICES = (
        ('BOIS', 'Bois'),
        ('TERRE', 'Terre'),
    )
    image = forms.ImageField(label="Photo", widget=forms.FileInput())
    firstname = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"size": 60}))
    lastname = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"size": 60}))
    date_of_birth = forms.DateField(label="Date de naissance")
    ambiance = forms.ModelChoiceField(label="Ambiance", queryset=Ambiance.objects.all(), empty_label="-----")
    code = forms.CharField(label="Code", widget=forms.TextInput(attrs={"size": 20}))

    class Meta:
        model = Students
        fields = ['image', 'firstname', 'lastname', 'date_of_birth', 'ambiance', 'code']

