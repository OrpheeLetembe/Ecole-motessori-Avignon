from django.urls import reverse, resolve
from authentication.views import SignUpView, login_page, logout_page


def test_signup_url():
    """
        Testing if the 'signup' route is mapping to SignUpView
    """
    url = reverse("signup")
    assert resolve(url).view_name == 'signup'
    assert resolve(url).func.view_class == SignUpView


def test_login_url():
    """
        Testing if the 'login' route is mapping to LoginView
    """
    url = reverse("login")
    assert resolve(url).view_name == 'login'
    assert resolve(url).func == login_page


def test_logout_url():
    """
        Testing if the 'logout' route is mapping to logout_page
    """
    url = reverse("logout")
    assert resolve(url).view_name == 'logout'
    assert resolve(url).func == logout_page

