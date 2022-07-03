import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from ambiance.models import Ambiance
from three_six.models import PracticalLife, SensoryMaterial, Math, Langage, Letter
from . import forms
from .models import Students


@login_required
def add_student(request, ambiance_id):
    """
    This function allows the creation of a new child object,
    as well as the creation of the practical life, sensory material,
    mathematics, language and letter objects associated with it
    """
    ambiance = Ambiance.objects.get(id=ambiance_id)
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.ambiance = ambiance
            pratique_life_create = PracticalLife.objects.create()
            sensorial_material_create = SensoryMaterial.objects.create()
            mathe_create = Math.objects.create()
            langage_create = Langage.objects.create()
            letter_create = Letter.objects.create()
            student.pratique_life = pratique_life_create
            student.sensorial_material = sensorial_material_create
            student.mathe = mathe_create
            student.langage = langage_create
            student.letter = letter_create
            student.save()
            return redirect('all_child', ambiance_id=ambiance.id)

    context = {
        'form': form,
        'ambiance': ambiance
    }

    return render(request, 'students/add_child.html', context=context)


@login_required
def students_ambiance_list(request, ambiance_id):
    """ This function is used to obtain the list of children in the same environment as the connected user"""

    ambiance = Ambiance.objects.get(id=ambiance_id)
    students = Students.objects.filter(ambiance=ambiance).order_by('lastname')

    context = {
        'ambiance': ambiance,
        'students': students,
        'user': request.user,
    }
    return render(request, 'students/ambiance_child_all.html', context=context)


@login_required
def student_active(request, ambiance_id):

    students = Students.objects.filter(active=True)
    ambiance = Ambiance.objects.get(id=ambiance_id)
    context = {
        'students': students,
        'ambiance': ambiance
    }
    return render(request, 'students/child_all.html', context=context)


@login_required
def update_student(request, student_id):
    """ This function allows you to update the information of a child """

    student = Students.objects.get(id=student_id)
    photo = student.photo.path
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            if student.tracker.has_changed('photo'):
                os.remove(photo)
            return redirect('all_child', ambiance_id=student.ambiance.id)
    else:
        form = forms.StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/update_student.html', context)


def trim_choice(data, activity):
    """This function allows you to choose the observations to be printed according to the quarter.
     It takes in parameter the data of the post request
     and the desired activity and returns the observations of the quarter.
     """

    if data is not None:
        if data == "observations_1":
            trimestre = activity.observations_1
            return trimestre
        if data == "observations_2":
            trimestre = activity.observations_2
            return trimestre
        if data == "observations_3":
            trimestre = activity.observations_3
            return trimestre
    else:
        return ""


@login_required
def student_bilan_pdf_view(request, pk):
    """ This function allows the creation of a child’s report in pdf format."""
    user = request.user
    student = Students.objects.get(pk=pk)
    today = date.today()
    form = forms.PrintFrom()
    if request.method == "POST":
        form = forms.PrintFrom(request.POST)
        if form.is_valid():
            trim_pratique_life = request.POST.get('pratique_life')
            trim_sensorial_material = request.POST.get('sensorial_material')
            trim_mathe = request.POST.get('mathe')
            trim_langage = request.POST.get('langage')
            pls = trim_choice(trim_pratique_life, student.pratique_life)
            mss = trim_choice(trim_sensorial_material, student.sensorial_material)
            mathes = trim_choice(trim_mathe, student.mathe)
            lang = trim_choice(trim_langage, student.langage)
            template_path = 'students/pdf1.html'
            context = {
                'user': user,
                'student': student,
                'today': today,
                'pls': pls,
                'mss': mss,
                'mathes': mathes,
                'lang': lang,
                'form': form
            }
            response = HttpResponse(content_type='application/pdf')
            filename = "{}_{}".format(student, student.ambiance)
            response['Content-Disposition'] = 'attachment; filename=Bilan_%s.pdf' % filename
            template = get_template(template_path)
            html = template.render(context)

            pisa_status = pisa.CreatePDF(
               html, dest=response)

            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
    context = {
        'form': form,
        'student': student

    }
    return render(request, 'students/choice_print.html', context=context)


@login_required
def student_doc_pdf_view(request, pk):
    """ This function allows the export of a child’s file in pdf format."""

    student = Students.objects.get(pk=pk)
    pls = student.pratique_life
    mss = student.sensorial_material
    mathes = student.mathe
    lang = student.langage
    lt = student.letter
    template_path = 'students/pdf2.html'
    context = {
        'student': student,
        'pls': pls,
        'mss': mss,
        'mts': mathes,
        'lang': lang,
        'lt': lt
    }
    response = HttpResponse(content_type='application/pdf')
    filename = "{}_{}".format(student, student.ambiance.year)
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
