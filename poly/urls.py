from django.urls import path
from poly.views import patient

app_name = 'poly'


urlpatterns = [
    path('patient/list', patient.PatientList.as_view(), name='patient-list'),
    path('patient/add/', patient.PatientCreate.as_view(), name='patient-add'),
    path('patient/delete/<int:pk>', patient.PatientDelete.as_view(), name='patient-delete'),
    path('patient/json/', patient.patient_json, name='patient-json'),
]
