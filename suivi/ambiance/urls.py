from django.urls import path

from . import views

urlpatterns = [
    path("", views.ambiance_list, name='ambiance'),
    path("ambiance/<int:ambiance_id>/student/<int:student_id>", views.add_student, name='ambiance_add_old'),
]
