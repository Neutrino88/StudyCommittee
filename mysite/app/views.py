from django.shortcuts import render
from django.http import HttpResponse

from .models import University


def index(request):
    universities = University.objects.order_by('short_name')[:20]
    context = {'universities': universities}
    return render(request, 'app/index.html', context)


def university_page(request, univ_id):
    return HttpResponse(f"University with id {univ_id}")


def faculty_page(request, fac_id):
    response = f"faculty id = {fac_id}"
    return HttpResponse(response)


def speciality_page(request, spec_id):
    response = f"spec_id = {spec_id}"
    return HttpResponse(response)


def group_page(request, group_id):
    response = f"group_id = {group_id}"
    return HttpResponse(response)
