from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class PatientInformation(models.Model):
  firstName=models.CharField(max_length=50,null=True,default='')
  lastName=models.CharField(max_length=50,null=True,default='')
  age=models.IntegerField( null=True,default='')
  gender=models.CharField(max_length=50,null=True,default='')
  woreda=models.CharField(max_length=50,null=True,default='')
  zone=models.CharField(max_length=50,null=True,default='')
  region=models.CharField(max_length=50,null=True,default='')
  job=models.CharField(max_length=50,null=True,default='')
  patientId=models.CharField( max_length=30,default='',unique=True,primary_key=True)
  updated=models.DateTimeField(auto_now=True)
  created=models.DateTimeField(auto_now_add=True)   
 
  def __str__(self):
        return self.firstName[0:10] +" "+self.lastName

  class Meta:
       ordering=['-updated'] 


# Laboratory Results
class LaboratoryMeasurement(models.Model):
     patientInformation = models.OneToOneField(PatientInformation,on_delete=models.CASCADE,null=False,default="0", primary_key=True)
     sbp=models.IntegerField(null=True,default='')
     fbs=models.IntegerField( null=True,default='')
     hw=models.CharField(max_length=50,null=True,default='')
     physcialActivity=models.CharField(max_length=50,null=True,default='')
     diabeticFamilyHistory=models.CharField(max_length=50,null=True,default='')
     impairedGlucose=models.CharField(max_length=50,null=True,default='')
     autoImune=models.CharField(max_length=50,null=True,default='')
     acuteWeightLoss=models.CharField(max_length=50,null=True,default='')  
     hypertension=models.CharField(max_length=50,null=True,default='')
     bmi=models.CharField(max_length=50,null=True,default='')
     monofilamenTest=models.CharField(max_length=50,null=False,default='')
     neurologicPain=models.CharField(max_length=50,null=False,default='')
     disautonomia=models.CharField(max_length=50,null=False,default='')
     footDeformity=models.CharField(max_length=50,null=False,default='')
     pad=models.CharField(max_length=50,null=False,default='')
     decreasedVision=models.CharField(max_length=50,null=False,default='')
     floaters=models.CharField(max_length=50,null=False,default='')
     retinalScreeningResult=models.CharField(max_length=50,null=False,default='')

     def __str__(self):
            return self.bmi+ " "+self.patientInformation.firstName

class PredictionResult(models.Model):
      patientInformation = models.OneToOneField(PatientInformation,on_delete=models.CASCADE,null=False,default="0", primary_key=True)
      diabetic=models.CharField(null=False,default='',max_length=50)
      risk=models.CharField(null=False,default='',max_length=50)
      neuropathy=models.CharField(null=False,default='',max_length=50)
      opthalmopathy=models.CharField(null=False,default='',max_length=50)

      def __str__(self):
            return self.diabetic+ " "+self.patientInformation.firstName

 
  



