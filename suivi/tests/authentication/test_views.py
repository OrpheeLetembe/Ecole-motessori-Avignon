from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

from ambiance.models import Ambiance


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.mark.django_db
def test_signup(client):
    """
    In the first assert, we are checing if a user is created successfully then,
    the user is redirected to '/ambiances/' route,
    For the second assert, we are checking the 302 status code(redirect)
    """

    ambiance = Ambiance.objects.create(name='Terre', year='2022/2023')
    credentials = {
        'username': 'TestUser',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'test-password',
        'password2': 'test-password',
        'role': 'educator',
        'ambiance': ambiance

    }
    client.post('/Inscription/', credentials)
    response = client.login(username=credentials['username'], password=credentials['password1'])
    print(response)
    assert response == True
    assert response.status_code == 302

