from django.urls import path
from poly.views import patient, clinic

app_name = 'poly'


urlpatterns = [
    path('patient/list', patient.PatientList.as_view(), name='patient-list'),
    path('patient/add/', patient.PatientCreate.as_view(), name='patient-add'),
    path('patient/delete/<int:pk>', patient.patient_delete, name='patient-delete'),
    path('patient/detail/<int:pk>', patient.PatientDetail.as_view(), name='patient-detail'),
    path('patient/edit/<int:pk>', patient.PatientEdit.as_view(), name='patient-edit'),
    path('patient/json/', patient.patient_json, name='patient-json'),

    path('clinic/list', clinic.ClinicList.as_view(), name='clinic-list'),
    path('clinic/add/', clinic.ClinicCreate.as_view(), name='clinic-add'),
    path('clinic/delete/<int:pk>', clinic.clinic_delete, name='clinic-delete'),
    path('clinic/detail/<int:pk>', clinic.ClinicDetail.as_view(), name='clinic-detail'),
    path('clinic/edit/<int:pk>', clinic.ClinicEdit.as_view(), name='clinic-edit'),
    path('clinic/json/', clinic.clinic_json, name='clinic-json'),
]
