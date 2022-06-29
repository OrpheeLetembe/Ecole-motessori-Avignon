from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404

from . import forms
from ambiance.models import Ambiance


def login_page(request, ambiance_id):
    """his function allows a registered user to log in.
    After verifying his credentials, the user is redirected to the feed page if they are correct.
    """
    ambiance = Ambiance.objects.get(id=ambiance_id)
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect('all_child', ambiance_id=ambiance.id)
            else:
                message = "Identifiants invalides."
    context = {
        'form': form,
         'message': message,
        'ambiance': ambiance
    }
    return render(request, "authentication/login.html", context=context)


def signup_page(request, ambiance_id):
    """This function allows the registration of a new user.
    After entering his credentials, the user is redirected to the feed page.
    """
    ambiance = Ambiance.objects.get(id=ambiance_id)
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.ambiance = ambiance
            user.save()
            login(request, user)
            return redirect('all_child', ambiance_id=ambiance.id)

    context = {
        'ambiance': ambiance,
        'form': form,
    }

    return render(request, "authentication/signup.html", context=context)


def logout_page(request):
    """Function allowing the disconnection of a user.
    After disconnection, the user is redirected to the login page
    """
    logout(request)
    return redirect('ambiance')


