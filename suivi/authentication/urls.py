from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("login", views.login_page, name='login'),
    path('login/parent', views.login_parent, name='parent'),
    path('Inscription/', views.signup_page, name='signup'),
    path('Déconnexion/', views.logout_page, name='logout'),

]