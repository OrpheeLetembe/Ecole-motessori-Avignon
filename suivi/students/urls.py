from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("child/add", views.add_student, name='add_child'),
    path("child/all", views.students_list, name='all_child'),
    path("student_change/<int:student_id>", views.update_student, name='student_change'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
