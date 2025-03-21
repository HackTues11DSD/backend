# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# from .models import Symptom, Cause

# def injuries(request):
#     symptomss = Symptom.objects.all().values()
#     causess = Cause.objects.all().values()
#     template = loader.get_template('basic_display_all.html')
#     context = {
#         'causess': causess,
#         'symptomss': symptomss,
#         }
#     return HttpResponse(template.render(context, request))


from rest_framework import viewsets
from .models import Injury, Symptom
from .serializers import InjurySerializer, SymptomSerializer

class InjuryViewSet(viewsets.ModelViewSet):
	queryset = Injury.objects.all()
	serializer_class = InjurySerializer

class SymptomViewSet(viewsets.ModelViewSet):
	queryset = Symptom.objects.all()
	serializer_class = SymptomSerializer

