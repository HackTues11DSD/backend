from rest_framework import serializers
from .models import Injury, Symptom

class InjurySerializer(serializers.ModelSerializer):
	class Meta:
		model = Injury
		fields = ['name']

class SymptomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields = ['name', 'place', 'cause']