from authentication.models import User
from ambiance.models import Ambiance


import pytest


@pytest.mark.django_db
def test_user_str():

    """
    Testing whether User's __str__ method is implemented properly
    """
    ambiance = Ambiance.objects.create(name='Terre', year='2022/2023')
    user = User.objects.create(
        username='TestUser',
        first_name='Test',
        last_name='User',
        ambiance=ambiance,
        role='educator',
        password='test-password',

    )

    assert str(user) == f'{user.first_name} {user.last_name}'
