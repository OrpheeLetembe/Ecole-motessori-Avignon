from django.shortcuts import render, redirect
from authentication.models import User
from students.models import Students

from . import forms
from .models import PracticalLife, SensoryMaterial, Math, Langage, Letter, Comments


def prat_life_view(request, student_id):
    student = Students.objects.get(id=student_id)
    practical_life_student = PracticalLife.objects.get(student=student)
    context = {
        'student': student,
        'pls': practical_life_student

    }

    return render(request, 'three_six/praticlife.html', context)


def update_prat_life(request, student_id):

    student = Students.objects.get(id=student_id)
    pratical_life_student = PracticalLife.objects.get(student=student)
    if request.method == 'POST':
        form = forms.PracticalLifeForm(request.POST, instance=pratical_life_student)
        if form.is_valid():
            form.save()
            return redirect('Vie_Pratique', student_id=student_id)
    else:
        form = forms.PracticalLifeForm(instance=pratical_life_student)
    context = {
        'form': form,
        'pls': pratical_life_student,
        'student': student
    }
    return render(request, 'three_six/update_VP.html', context)


def sensorial_view(request, student_id):
    student = Students.objects.get(id=student_id)
    sensoryal_mat = SensoryMaterial.objects.get(student=student)

    context = {
        'student': student,
        'mss': sensoryal_mat,

    }

    return render(request, 'three_six/sensorial.html', context)


def update_mat_sen(request, student_id):

    student = Students.objects.get(id=student_id)
    material_sensorial_student = SensoryMaterial.objects.get(student=student)
    if request.method == 'POST':
        form = forms.SensoryMaterialForm(request.POST, instance=material_sensorial_student)
        if form.is_valid():
            form.save()
            return redirect('Materiel_sensoriel', student_id=student_id)
    else:
        form = forms.SensoryMaterialForm(instance=material_sensorial_student)
    context = {
        'form': form,
        'mss': material_sensorial_student,
        'student': student
    }
    return render(request, 'three_six/update_MS.html', context)


def math_view(request, student_id):
    student = Students.objects.get(id=student_id)
    mathematique = Math.objects.get(student=student)

    context = {
        'student': student,
        'mts': mathematique,

    }

    return render(request, 'three_six/math.html', context)


def update_math(request, student_id):

    student = Students.objects.get(id=student_id)
    math_student = Math.objects.get(student=student)
    if request.method == 'POST':
        form = forms.MathForm(request.POST, instance=math_student)
        if form.is_valid():
            form.save()
            return redirect('Mathematiques', student_id=student_id)
    else:
        form = forms.MathForm(instance=math_student)
    context = {
        'form': form,
        'mts': math_student,
        'student': student
    }
    return render(request, 'three_six/update_MATH.html', context)


def langage_view(request, student_id):
    student = Students.objects.get(id=student_id)
    langage = Langage.objects.get(student=student)
    letter = Letter.objects.get(student=student)

    context = {
        'student': student,
        'lang': langage,
        'let': letter

    }

    return render(request, 'three_six/langage.html', context)


def update_langage(request, student_id):

    student = Students.objects.get(id=student_id)
    langage_student = Langage.objects.get(student=student)
    letter_student = Letter.objects.get(student=student)
    if request.method == 'POST':
        langage_form = forms.LangageForm(request.POST, instance=langage_student)
        letter_form = forms.LetterForm(request.POST, instance=letter_student)
        if all([langage_form.is_valid(), letter_form.is_valid()]):
            langage_form.save()
            letter_form.save()
            return redirect('Langage', student_id=student_id)
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


def trim_view(request, student_id):
    student = Students.objects.get(id=student_id)
    trim = Comments.objects.get(student=student)
    context = {
        'student': student,
        'trim': trim

    }

    return render(request, 'three_six/trim.html', context)


def update_trim(request, student_id):

    student = Students.objects.get(id=student_id)
    trim_student = Comments.objects.get(student=student)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST, instance=trim_student)
        if form.is_valid():
            form.save()
            return redirect('Observations', student_id=student_id)
    else:
        form = forms.CommentForm(instance=trim_student)
    context = {
        'form': form,
        'tim': trim_student,
        'student': student
    }
    return render(request, 'three_six/update_trim.html', context)
