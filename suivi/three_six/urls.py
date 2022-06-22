from django.urls import path


from . import views

urlpatterns = [
    path("Vie_Pratique/<int:student_id>", views.prat_life_view, name='Vie_Pratique'),
    path("Vie_Pratique_change/<int:student_id>", views.update_prat_life, name='Vie_Pratique_change'),
    path("Materiel_sensoriel/<int:student_id>", views.sensorial_view, name='Materiel_sensoriel'),
    path("Materiel_sensoriel_change/<int:student_id>", views.update_mat_sen, name='Materiel_sensoriel_change'),
    path("Mathematiques/<int:student_id>", views.math_view, name='Mathematiques'),
    path("Mathematiques_change/<int:student_id>", views.update_math, name='Mathematiques_change'),
    path("Langage/<int:student_id>", views.langage_view, name='Langage'),
    path("Langage_change/<int:student_id>", views.update_langage, name='Langage_change'),
    path("Observations/<int:student_id>", views.trim_view, name='Observations'),
    path("Observations_change/<int:student_id>", views.update_trim, name='Observations_change'),
    ]
