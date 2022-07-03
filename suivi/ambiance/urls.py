from django.urls import path

from . import views

urlpatterns = [
    path("ambiance/ajouter", views.add_ambiance, name='add_ambiance'),
    path("ambiance", views.ambiance_list, name='ambiance'),
    path("ambiance/<int:ambiance_id>/student/<int:student_id>",
         views.add_student, name='ambiance_add_old'),
]
