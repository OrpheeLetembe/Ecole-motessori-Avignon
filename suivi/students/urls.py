from django.urls import path


from . import views

urlpatterns = [
    path("child/add/<int:ambiance_id>", views.add_student, name='add_child'),
    path("child/all/<int:ambiance_id>", views.students_ambiance_list, name='all_child'),
    path("student_change/<int:student_id>", views.update_student, name='student_change'),

    path("print_choice/<pk>", views.student_bilan_pdf_view, name='print_choice'),
    path("print/<pk>", views.student_doc_pdf_view, name='print'),

    path("ambiance/add_child/<int:ambiance_id>", views.student_active, name='ambiance_add_child'),

]
