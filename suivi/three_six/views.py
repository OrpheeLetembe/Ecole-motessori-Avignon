from django.shortcuts import render, redirect
from authentication.models import User
from students.models import Students

from . import forms
from .models import PracticalLife, SensoryMaterial, Langage, Letter


def add_prat_life_view(request, student_id):
    student = Students.objects.get(id=student_id)
    form = forms.PracticalLifeForm()
    if request.method == 'POST':
        form = forms.PracticalLifeForm(request.POST)
        if form.is_valid():
            pl = form.save(commit=False)
            pl.student = student
            pl.save()
            context = {
                'student': student,
                'pl': pl
            }
            return render(request, 'three_six/praticlife.html', context)

    return render(request, "three_six/add_update_VP.html", context={"form": form})


def update_prat_life(request, student_id):
    student = Students.objects.get(id=student_id)
    pl = PracticalLife.objects.get(student=student)
    if request.method == 'POST':
        form = forms.PracticalLifeForm(request.POST, instance=pl)
        if form.is_valid():
            form.save()
            return redirect('Vie_Pratique', student_id=student_id)
    else:
        form = forms.PracticalLifeForm(instance=pl)
        context = {
            'form': form,
            'pl': pl,
            'student': student
        }
        return render(request, 'three_six/add_update_VP.html', context)


def prat_life_view(request, student_id):
    student = Students.objects.get(id=student_id)
    practical_life = PracticalLife.objects.get(student=student)
    context = {
        'student': student,
        'pl': practical_life

    }

    return render(request, 'three_six/praticlife.html', context)


def langage_view(request, student_id):
    student = Students.objects.get(id=student_id)
    langage = Langage.objects.get(student=student)
    letter = Letter.objects.get(student=student)

    context = {
        'student': student,
        'lang': langage,
        'let': letter

    }

    return render(request, 'students/langage.html', context)


def sensorial_view(request, student_id):
    student = Students.objects.get(id=student_id)
    sensoryal_mat = SensoryMaterial.objects.get(student=student)

    context = {
        'student': student,
        'ms': sensoryal_mat,

    }

    return render(request, 'three_six/sensorial.html', context)
