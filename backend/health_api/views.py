from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Injury

def injuries(request):
    injuriess = Injury.objects.all().values()
    template = loader.get_template('basic_display_all.html')
    context = {'injuries': injuriess,}
    return HttpResponse(template.render(context, request))