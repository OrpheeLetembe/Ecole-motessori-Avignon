from django import forms
from .models import Students
from ambiance.models import Ambiance


class StudentForm(forms.ModelForm):

    photo = forms.ImageField(label="Photo", required=False, widget=forms.FileInput(attrs={"class": "form-control"}))
    firstname = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"class": "form-control"}))
    lastname = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"class": "form-control"}))
    date_of_birth = forms.DateField(
        label="Date de naissance", input_formats=['%d/%m/%Y'])
    ambiance = forms.ModelChoiceField(label="Ambiance", queryset=Ambiance.objects.all(), empty_label="-----",
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    profil = forms.CharField(
        label="Profil", required=False, widget=forms.Textarea(attrs={"rows": 8, "cols": 81, 'class': 'form-control'}))

    class Meta:
        model = Students
        fields = ['photo', 'firstname', 'lastname', 'date_of_birth', 'ambiance', 'profil']


class PrintFrom(forms.Form):
    CHOICES = (
        ('observations_1', 'Trimestre 1'),
        ('observations_2', 'Trimestre 2'),
        ('observations_3', 'Trimestre 3')
    )
    pratique_life = forms.ChoiceField(
        label="Vie Pratique", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    sensorial_material = forms.ChoiceField(
        label="Matériel Sensoriel", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    mathe = forms.ChoiceField(
        label="Mathématiques", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    langage = forms.ChoiceField(
        label="Langage", required=False,
        choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))

