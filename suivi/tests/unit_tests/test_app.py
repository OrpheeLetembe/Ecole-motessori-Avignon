from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

from authentication.forms import SignUpForm
from authentication.models import User


@pytest.fixture
def client():
    client = Client()
    return client


# Ensure that app was set up correctly
def test_index_page_loads(client):
    response = client.get('/')
    data = response.content.decode()
    assert response.status_code == 200
    assert '<title>Connection</title>' in data
    assert '<a href="/Inscription/">S\'enregistrer</a>' in data


@pytest.mark.django_db
def test_register_page_loads(client):

    response = client.get('/Inscription/')
    data = response.content.decode()
    assert response.status_code == 200
    assert '<title>Formulaire d\'enregistrement</title>' in data
    assert '<a href="/">Retour</a>' in data


@pytest.mark.django_db
def test_register_user(client):

    """
        Testing if the User object is created properly
        """

    temp_user = {
        'username': 'TestUser',
        'password1': 'test-password',
        'password2': 'test-password',
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User'
    }

    form = SignUpForm(data=temp_user)
    user = form.save()

    assert isinstance(user, User)



