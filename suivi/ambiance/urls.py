from django.urls import path

from . import views

urlpatterns = [
    path("", views.ambiance_list, name='ambiance'),

]
