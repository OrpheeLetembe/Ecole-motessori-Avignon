from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label="",
                               widget=forms.TextInput(attrs={"class": "user_name", "placeholder": "Nom d'utilisateur",
                                                             "size": 40}))
    password = forms.CharField(max_length=60, label="",
                               widget=forms.PasswordInput(attrs={"class": "pwd", "placeholder": "Mot de passe",
                                                                 "size": 40}))


class SignupForm(UserCreationForm):

    ENVIRONMENT_CHOICES = [
        ('Bois', 'Bois'),
        ('terre', 'Terre'),

    ]

    username = forms.CharField(required=True, label="Nom d'utilisateur", widget=forms.TextInput(attrs={"size": 60}))
    first_name = forms.CharField(label="Prénom", widget=forms.TextInput(attrs={"size": 60}))
    last_name = forms.CharField(label="Nom", widget=forms.TextInput(attrs={"size": 60}))
    phone = forms.CharField(label="Numéro de téléphone", widget=forms.TextInput(attrs={"size": 60}))
    ambiance = forms.ChoiceField(label='Ambiance', choices=ENVIRONMENT_CHOICES, widget=forms.RadioSelect())
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"size": 60}))
    password2 = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput(attrs={"size": 60}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
