from django.urls import path


app_name = 'api'
from . import views

app_name = 'api'
urlpatterns = [
    #  Basic Informations
    path('basic-info/', views.getPatientInformations),
    path('basic-info/<str:pk>/', views.getPatientInformation),
    path('basic-info/create/', views.createPatientInformation),
    path('basic-info/<str:pk>/update', views.updateBasic),
    # laboratory Informations
    path('lab/', views.getLab),
    path('lab/create/', views.createLaboratoryInformation),
    path('lab/<str:pk>/', views.getLaboratoryInformation),
    # Searching API
    path('patient/', views.SearchAPIView.as_view())
   
    
]