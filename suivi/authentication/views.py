from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404

from . import forms
from students.models import Students
from three_six.models import PracticalLife


def home_page(request):
    return render(request, "authentication/home.html")


def logout_page(request):
    """Function allowing the disconnection of a user.
    After disconnection, the user is redirected to the login page
    """
    logout(request)
    return redirect('home')


def login_page(request):
    """his function allows a registered user to log in.
    After verifying his credentials, the user is redirected to the feed page if they are correct.
    """
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
                return redirect('all_child')
            else:
                message = "Identifiants invalides."
    return render(request, "authentication/login.html", context={"form": form, "message": message})


def signup_page(request):
    """This function allows the registration of a new user.
    After entering his credentials, the user is redirected to the feed page.
    """
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_child')

    return render(request, "authentication/signup.html", context={"form": form})


def login_parent(request):

    form = forms.ParentLoginForm()
    if request.method == 'POST':
        form = forms.ParentLoginForm(request.POST)
        if form.is_valid():
            try:
                student = Students.objects.get(code=form.data['code'])
                practical_life = PracticalLife.objects.get(student=student)
                context = {
                    'student': student,
                    'pl': practical_life
                }

                return render(request, 'three_six/praticlife.html', context)
            except Students.DoesNotExist:
                message = "Code invalide."
                return render(request, "authentication/login_parent.html", context={'form': form, 'message': message})

    return render(request, "authentication/login_parent.html", context={'form': form})


