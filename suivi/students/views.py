from django.shortcuts import render, redirect

from three_six.models import PracticalLife, SensoryMaterial, Math, Langage, Letter, Comments
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
            Comments.objects.create(student=student)

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


def update_student(request, student_id):

    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('all_child')
    else:
        form = forms.StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/update_student.html', context)

