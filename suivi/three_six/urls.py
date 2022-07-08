from django.urls import path


from . import views

urlpatterns = [
    path("Vie_Pratique_change/<int:student_id>", views.update_prat_life,
         name='Vie_Pratique_change'),
    path("Materiel_sensoriel_change/<int:student_id>", views.update_mat_sen,
         name='Materiel_sensoriel_change'),
    path("Mathematiques_change/<int:student_id>", views.update_math,
         name='Mathematiques_change'),
    path("Langage_change/<int:student_id>", views.update_langage,
         name='Langage_change'),

    ]
