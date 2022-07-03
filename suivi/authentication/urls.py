from django.urls import path

from .views import SignUpView, login_page, logout_page

urlpatterns = [
    path("", login_page, name='login'),
    path('Inscription/', SignUpView.as_view(), name='signup'),
    path('Déconnexion/', logout_page, name='logout'),

]
