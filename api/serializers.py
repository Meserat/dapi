from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import PatientInformation,LaboratoryMeasurement, PredictionResult
from rest_framework import serializers

# define serializer 

class PatientInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = PatientInformation
    fields='__all__'


class LaboratoryMeasurementSerializer(serializers.ModelSerializer):
  
   class Meta:
    model = LaboratoryMeasurement
    fields='__all__'
    depth=1

class PredictionResultSerializer(serializers.ModelSerializer):
  
   class Meta:
    model = PredictionResult
    fields='__all__'
    depth=1





