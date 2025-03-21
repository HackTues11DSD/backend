from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Symptom, Cause

def injuries(request):
    symptomss = Symptom.objects.all().values()
    causess = Cause.objects.all().values()
    template = loader.get_template('basic_display_all.html')
    context = {
        'causess': causess,
        'symptomss': symptomss,
        }
    return HttpResponse(template.render(context, request))