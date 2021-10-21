from django.contrib import admin

# Register your models here.
from .models import PatientInformation, PredictionResult
from .models import LaboratoryMeasurement


admin.site.register([PatientInformation,LaboratoryMeasurement, PredictionResult])