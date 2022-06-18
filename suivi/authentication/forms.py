from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from ambiance.models import Ambiance


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="",
                               widget=forms.TextInput(attrs={"class": "user_name", "placeholder": "Nom d'utilisateur",
                                                             "size": 40}))
    password = forms.CharField(max_length=60, label="",
                               widget=forms.PasswordInput(attrs={"class": "pwd", "placeholder": "Mot de passe",
                                                                 "size": 40}))


class SignupForm(UserCreationForm):

    username = forms.CharField(required=True, label="Nom d'utilisateur", widget=forms.TextInput(attrs={"size": 60}))
    firstname = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"size": 60}))
    lastname = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"size": 60}))
    ambiance = forms.ModelChoiceField(label="Ambiance", queryset=Ambiance.objects.all())
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"size": 60}))
    password2 = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput(attrs={"size": 60}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class ParentLoginForm(forms.Form):
    code = forms.CharField(max_length=60, label="Code", widget=forms.PasswordInput(attrs={"size": 40}))
