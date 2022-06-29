from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from ambiance.models import Ambiance


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=60, label="Mot de passe",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class SignupForm(UserCreationForm):

    CHOICES = (
        ('educator', 'Educatrice'),
        ('assistant', 'Assistante')
    )

    username = forms.CharField(required=True, label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    firstname = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"class": "form-control"}))
    lastname = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"class": "form-control"}))
    role = forms.ChoiceField(
        label="Rôle", required=False,
        choices=CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
    # ambiance = forms.ModelChoiceField(
        # label="Ambiance", required=False, queryset=Ambiance.objects.all(), empty_label="-----",
        # widget=forms.Select(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirmer mot de passe",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()



