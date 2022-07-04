from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm, LoginForm


class SignUpView(CreateView):
    """
    User registration

    Form parameters:
        first_name (string): first name of an user
        last_name (string): last name of an user
        username (string): username of an user
        role (string): role of an user
        ambiance (object): ambiance of user
        password1 (password): new password of an user
        password2 (password): confirm new password of an user

    """
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/signup.html'


def login_page(request):
    """"
    his function allows a registered user to log in.
    After verifying his credentials, the user is redirected to the feed page if they are correct.

    """
    form = LoginForm()
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('ambiance')
            else:
                message = "Identifiants invalides."
    context = {
        'form': form,
         'message': message,

    }
    return render(request, "authentication/login.html", context=context)


def logout_page(request):
    """
    Function allowing the disconnection of a user.
    After disconnection, the user is redirected to the login page
    """
    logout(request)
    return redirect('login')


