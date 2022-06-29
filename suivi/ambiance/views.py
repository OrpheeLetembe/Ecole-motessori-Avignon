from django.shortcuts import render, redirect

from .models import Ambiance
from students.models import Students


def ambiance_list(request):
    """" This function allows you to get the list of atmospheres, the most recent ones first."""
    ambiances = Ambiance.objects.all().order_by('-date_created')
    return render(request, 'ambiance/all.html', context={'ambiances': ambiances})


def add_student(request, ambiance_id, student_id):
    """" This function allows you to add existing children to a new atmosphere."""
    ambiance = Ambiance.objects.get(id=ambiance_id)
    old_student = Students.objects.get(id=student_id)
    new_student = Students.objects.create(
        photo=old_student.photo,
        firstname=old_student.firstname,
        lastname=old_student.lastname,
        date_of_birth=old_student.date_of_birth,
        profil=old_student.profil,
        ambiance=ambiance,
        pratique_life=old_student.pratique_life,
        sensorial_material=old_student.sensorial_material,
        mathe=old_student.mathe,
        langage=old_student.langage,
        letter=old_student.letter
    )
    new_student.save()
    return redirect('all_child', ambiance_id=ambiance.id)
