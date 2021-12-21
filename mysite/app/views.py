from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from .models import University, Faculty, Speciality, StudyGroup, Discipline, Lecturer


def index(request):
    universities = University.objects.order_by('short_name')[:20]
    context = {'universities': universities}
    return render(request, 'app/index.html', context)


def university_page(request, univ_id):
    try:
        university = University.objects.get(pk=univ_id)
    except University.DoesNotExist:
        raise Http404("University does not exist")

    return render(request, 'app/university.html', {'university': university})


def faculty_page(request, fac_id):
    try:
        faculty = Faculty.objects.get(pk=fac_id)
    except Faculty.DoesNotExist:
        raise Http404("Faculty does not exist")

    return render(request, 'app/faculty.html', {'faculty': faculty})


def speciality_page(request, spec_id):
    try:
        speciality = Speciality.objects.get(pk=spec_id)
    except Speciality.DoesNotExist:
        raise Http404("Speciality does not exist")

    return render(request, 'app/speciality.html', {'speciality': speciality})


@login_required
def group_page(request, group_id):
    try:
        group = StudyGroup.objects.get(pk=group_id)
    except StudyGroup.DoesNotExist:
        raise Http404("Study group does not exist")

    return render(request, 'app/group.html', {'group': group})


def discipline_page(request, disc_id):
    try:
        discipline = Discipline.objects.get(pk=disc_id)
    except StudyGroup.DoesNotExist:
        raise Http404("Discipline does not exist")

    return render(request, 'app/discipline.html', {'discipline': discipline})


@login_required
def lecturer_page(request, lect_id):
    try:
        lecturer = Lecturer.objects.get(pk=lect_id)
    except Lecturer.DoesNotExist:
        raise Http404("Discipline does not exist")

    return render(request, 'app/lecturer.html', {'lecturer': lecturer})
