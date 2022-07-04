from ambiance.models import Ambiance
from authentication.models import User

from authentication.forms import SignUpForm

import pytest


@pytest.mark.django_db
def test_signup_form_validate():

    """
    Testing the SignUpForm to check if the user input data is properly validated or not
    """

    ambiance = Ambiance.objects.create(name='Terre', year='2022/2023')
    temp_user = {
        'username': 'TestUser',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'test-password',
        'password2': 'test-password',
        'role': 'educator',
        'ambiance': ambiance

    }

    user = SignUpForm(data=temp_user)

    assert user.is_valid()


@pytest.mark.django_db
def test_signup_form_save_method():

    """
    Testing if the User object is created properly by using SignUpForm or not
    """
    ambiance = Ambiance.objects.create(name='Terre', year='2022/2023')
    temp_user = {
        'username': 'TestUser',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'test-password',
        'password2': 'test-password',
        'role': 'educator',
        'ambiance': ambiance

    }

    form = SignUpForm(data=temp_user)
    user = form.save()

    assert isinstance(user, User)
