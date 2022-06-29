from django.urls import path


from . import views

urlpatterns = [
    path("child/add/<int:ambiance_id>", views.add_student, name='add_child'),
    path("child/all/<int:ambiance_id>", views.students_list, name='all_child'),
    path("student_change/<int:student_id>", views.update_student, name='student_change'),

    path("print_choice/<pk>", views.student_pdf_view, name='print_choice'),
    #path("print/<pk>", views.student_pdf_view, name='print'),

]


