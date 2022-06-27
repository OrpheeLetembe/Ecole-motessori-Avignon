from django.contrib.auth.models import User
#from authentication.models import User
from authentication.forms import SignupForm
from ambiance.models import Ambiance

import pytest

@pytest.mark.django_db
def test_signup_form_validate():

    """
    Testing the SignUpForm to check if the user input data is properly validated or not
    """
    ambiance = Ambiance.objects.create(name='Bois', year=2015)

    temp_user = {
        'username': 'TestUser',
        'password1': 'test-password123',
        'password2': 'test-password123',
        'ambiance': ambiance,
        'firstname': 'Test',
        'lastname': 'User'
    }

    user = SignupForm(data=temp_user)

    assert user.is_valid()


@pytest.mark.django_db
def test_signup_form_save_method():

    """
    Testing if the User object is created properly by using SignUpForm or not
    """
    ambiance = Ambiance.objects.create(name='Bois', year=2015)
    temp_user = {
        'username': 'TestUser',
        'password1': 'test-password123',
        'password2': 'test-password123',
        'ambiance': ambiance,
        'firstname': 'Test',
        'lastname': 'User'
    }

    form = SignupForm(data=temp_user)
    user = form.save()

    assert isinstance(user, User)
