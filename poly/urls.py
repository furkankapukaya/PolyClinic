from django.urls import path
from poly.views import patient, clinic, doctor, appointment, treatment

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

    path('doctor/list', doctor.DoctorList.as_view(), name='doctor-list'),
    path('doctor/add/', doctor.DoctorCreate.as_view(), name='doctor-add'),
    path('doctor/delete/<int:pk>', doctor.doctor_delete, name='doctor-delete'),
    path('doctor/detail/<int:pk>', doctor.DoctorDetail.as_view(), name='doctor-detail'),
    path('doctor/edit/<int:pk>', doctor.DoctorEdit.as_view(), name='doctor-edit'),
    path('doctor/json/', doctor.doctor_json, name='doctor-json'),

    path('appointment/list', appointment.AppointmentList.as_view(), name='appointment-list'),
    path('appointment/add/', appointment.AppointmentCreate.as_view(), name='appointment-add'),
    path('appointment/delete/<int:pk>', appointment.appointment_delete, name='appointment-delete'),
    path('appointment/detail/<int:pk>', appointment.AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointment/edit/<int:pk>', appointment.AppointmentEdit.as_view(), name='appointment-edit'),
    path('appointment/json/', appointment.appointment_json, name='appointment-json'),

    path('treatment/list', treatment.TreatmentList.as_view(), name='treatment-list'),
    path('treatment/add/<int:pk>', treatment.treatment_create, name='treatment-add'),
    path('treatment/delete/<int:pk>', treatment.treatment_delete, name='treatment-delete'),
    path('treatment/detail/<int:pk>', treatment.TreatmentDetail.as_view(), name='treatment-detail'),
    path('treatment/edit/<int:pk>', treatment.TreatmentEdit.as_view(), name='treatment-edit'),
    path('treatment/json/', treatment.treatment_json, name='treatment-json'),
]
