from django.urls import path

from . import views

urlpatterns = [
    path("ambiance/ajouter", views.add_ambiance_view, name='add_ambiance'),
    path("ambiance", views.ambiance_list_view, name='ambiance'),
    path("ambiance/<int:ambiance_id>/student/<int:student_id>",
         views.add_student, name='ambiance_add_old'),
]
