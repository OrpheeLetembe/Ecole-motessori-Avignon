from django import forms
from .models import Students
from ambiance.models import Ambiance


class StudentForm(forms.ModelForm):

    image = forms.ImageField(label="Photo", required=False, widget=forms.FileInput(attrs={"class": "form-control"}))
    firstname = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"class": "form-control"}))
    lastname = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"class": "form-control"}))
    date_of_birth = forms.DateField(label="Date de naissance")
    ambiance = forms.ModelChoiceField(label="Ambiance", queryset=Ambiance.objects.all(), empty_label="-----",
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Students
        fields = ['image', 'firstname', 'lastname', 'date_of_birth', 'ambiance']

