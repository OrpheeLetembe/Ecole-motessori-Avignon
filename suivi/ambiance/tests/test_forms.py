from ambiance.forms import AmbianceForm
from ambiance.models import Ambiance

import pytest


@pytest.mark.django_db
def test_ambiance_form_validate():

    """
    Testing the SignUpForm to check if the user input data is properly validated or not
    """

    temp_ambiance = {
        'name': 'Terre',
        'year': '2022/2023',
    }

    ambiance = AmbianceForm(data=temp_ambiance)

    assert ambiance.is_valid()


@pytest.mark.django_db
def test_ambiance_form__save_method():

    """
    Testing if the Ambiance object is created properly by using AmbianceForm or not
    """

    temp_ambiance = {
        'name': 'Terre',
        'year': '2022/2023',
    }

    form = AmbianceForm(data=temp_ambiance)
    ambiance = form.save()

    assert isinstance(ambiance, Ambiance)

