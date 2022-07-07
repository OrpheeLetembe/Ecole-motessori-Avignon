from django.urls import reverse, resolve
from ambiance.views import add_ambiance, ambiance_list, add_student


def test_all_ambiance_url():
    """
        Testing if the 'ambiance' route is mapping to ambiance_list
    """
    url = reverse("ambiance")
    assert resolve(url).view_name == 'ambiance'
    assert resolve(url).func == ambiance_list


def test_add_ambiance_url():
    """
        Testing if the 'add_ambiance' route is mapping to ambiance_list
    """
    url = reverse("add_ambiance")
    assert resolve(url).view_name == 'add_ambiance'
    assert resolve(url).func == add_ambiance
