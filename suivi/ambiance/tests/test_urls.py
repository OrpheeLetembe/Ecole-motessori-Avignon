from django.urls import reverse, resolve
from ambiance.views import add_ambiance_view, ambiance_list_view


def test_add_ambiance_url():
    """
        Testing if the 'add_ambiance' route is mapping to add_ambiance_view
    """
    url = reverse("add_ambiance")
    assert resolve(url).view_name == 'add_ambiance'
    assert resolve(url).func == add_ambiance_view


def test_ambiance_list_url():
    """
        Testing if the 'ambiance' route is mapping to ambiance_list_view
    """
    url = reverse("ambiance")
    assert resolve(url).view_name == 'ambiance'
    assert resolve(url).func == ambiance_list_view
