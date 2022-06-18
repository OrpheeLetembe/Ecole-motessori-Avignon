from django.urls import path


from . import views

urlpatterns = [
    path("Vie_Pratique/<int:student_id>", views.prat_life_view, name='Vie_Pratique'),
    path("Vie_Pratique_change/<int:student_id>", views.update_prat_life, name='Vie_Pratique_change'),

    ]
