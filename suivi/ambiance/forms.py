from django import forms

from .models import Ambiance


class AmbianceForm(forms.ModelForm):
    year = forms.CharField(required=True, label="Année scolaire",
                           widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Ambiance
        exclude = ('name', )
