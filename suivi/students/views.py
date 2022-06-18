from django.shortcuts import render, redirect

from three_six.models import PracticalLife, SensoryMaterial, Math, Langage, Letter
from . import forms
from .models import Students


def add_student(request):

    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            student.save()
            PracticalLife.objects.create(student=student)
            SensoryMaterial.objects.create(student=student)
            Math.objects.create(student=student)
            Langage.objects.create(student=student)
            Letter.objects.create(student=student)

            return redirect('all_child')

    return render(request, 'students/add_child.html', context={'form': form})


def students_list(request):

    ambiance = request.user.ambiance
    students = Students.objects.filter(ambiance=ambiance).order_by('lastname')
    context = {
        'ambiance': ambiance,
        'students': students,
        'user': request.user
    }
    return render(request, 'students/all.html', context=context)





