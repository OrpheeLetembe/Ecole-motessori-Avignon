from django.urls import path

from . import views

urlpatterns = [
    path("login/<int:ambiance_id>", views.login_page, name='login'),
    path('Inscription/<int:ambiance_id>', views.signup_page, name='signup'),
    path('Déconnexion/', views.logout_page, name='logout'),

]
