from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Ambiance
from .forms import AmbianceForm
from students.models import Students


@login_required
def add_ambiance(request):
    """This function allows the connected user to add a new school year to his atmosphere"""

    ambiance_name = request.user.ambiance.name
    form = AmbianceForm()
    if request.method == 'POST':
        form = AmbianceForm(request.POST)
        if form.is_valid():
            ambiance = form.save(commit=False)
            ambiance.name = ambiance_name
            ambiance.save()
            return redirect('ambiance')
    context = {
        'ambiance': ambiance_name,
        'form': form,
    }
    return render(request, 'ambiance/add_ambiance.html', context=context)


@login_required
def ambiance_list(request):
    """" This function allows you to get the list of atmospheres, the most recent ones first."""

    user = request.user
    ambiances = Ambiance.objects.filter(name=user.ambiance.name).order_by('-date_created')
    return render(request, 'ambiance/ambiance_all.html', {'ambiances': ambiances})


@login_required
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
    old_student.deactivate()
    new_student.save()
    return redirect('all_child', ambiance_id=ambiance.id)
