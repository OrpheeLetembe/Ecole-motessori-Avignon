from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from students.models import Students

from . import forms


@login_required
def update_prat_life(request, student_id):

    student = Students.objects.get(id=student_id)
    pratique_life_student = student.pratique_life
    if request.method == 'POST':
        form = forms.PracticalLifeForm(request.POST, instance=pratique_life_student)
        if form.is_valid():
            form.save()
            return redirect('Vie_Pratique_change', student_id=student_id)
    else:
        form = forms.PracticalLifeForm(instance=pratique_life_student)
    context = {
        'form': form,
        'pls': pratique_life_student,
        'student': student
    }
    return render(request, 'three_six/update_VP.html', context)


@login_required
def update_mat_sen(request, student_id):

    student = Students.objects.get(id=student_id)
    material_sensorial_student = student.sensorial_material
    if request.method == 'POST':
        form = forms.SensoryMaterialForm(request.POST, instance=material_sensorial_student)
        if form.is_valid():
            form.save()
            return redirect('Materiel_sensoriel_change', student_id=student_id)
    else:
        form = forms.SensoryMaterialForm(instance=material_sensorial_student)
    context = {
        'form': form,
        'mss': material_sensorial_student,
        'student': student
    }
    return render(request, 'three_six/update_MS.html', context)


@login_required
def update_math(request, student_id):

    student = Students.objects.get(id=student_id)
    math_student = student.mathe
    if request.method == 'POST':
        form = forms.MathForm(request.POST, instance=math_student)
        if form.is_valid():
            form.save()
            return redirect('Mathematiques_change', student_id=student_id)
    else:
        form = forms.MathForm(instance=math_student)
    context = {
        'form': form,
        'mts': math_student,
        'student': student
    }
    return render(request, 'three_six/update_MATH.html', context)


@login_required
def update_langage(request, student_id):

    student = Students.objects.get(id=student_id)
    langage_student = student.langage
    letter_student = student.letter
    if request.method == 'POST':
        langage_form = forms.LangageForm(request.POST, instance=langage_student)
        letter_form = forms.LetterForm(request.POST, instance=letter_student)
        if all([langage_form.is_valid(), letter_form.is_valid()]):
            langage_form.save()
            letter_form.save()
            return redirect('Langage_change', student_id=student_id)
    else:
        langage_form = forms.LangageForm(instance=langage_student)
        letter_form = forms.LetterForm(instance=letter_student)

    context = {
        'langage_form': langage_form,
        'letter_form': letter_form,
        'mts': langage_student,
        'student': student
    }
    return render(request, 'three_six/update_langage.html', context)
