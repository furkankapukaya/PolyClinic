from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy

from poly.forms.appointment import AppointmentForm
from poly.models import Appointment, Clinic, Patient, Doctor


def appointment_json(request):
    data = []
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    items = Appointment.objects.all()
    records_total = items.count()
    items = items[start:length]
    records_filtered = items.count()
    for item in items:
        data.append([
            item.patient.name + ' ' + item.patient.surname,
            item.doctor.name + ' ' + item.doctor.surname,
            item.date,
            item.get_hour_display(),
            '<a href="/treatment/add/' + str(item.id) + '" class="btn btn-primary btn-xs"><i class="fa fa-medkit">'
            '</i> Tedavi</a>'
            '<a href="/appointment/edit/' + str(item.id) + '" class="btn btn-info btn-xs">'
            '<i class="fa fa-pencil"></i> Düzenle </a>'
            '<a href="/appointment/delete/' + str(item.id) + '" class="btn btn-danger btn-xs">'
            '<i class="fa fa-trash-o"></i> Sil </a>'
        ])
    return JsonResponse({
        'recordsTotal': records_total,
        'recordsFiltered': records_filtered,
        'data': data
    }, safe=False)


class AppointmentList(ListView):
    template_name = 'poly/appointment/list.html'
    context_object_name = 'appointment_list'

    def get_queryset(self):
        if self.request.is_ajax():
            return JsonResponse(list(Appointment.objects.all().values('patient', 'doctor', 'date', 'hour')), safe=False)
        return None


class AppointmentDetail(DetailView):
    model = Appointment
    template_name = 'poly/appointment/detail.html'
    extra_context = {'doctors': Doctor.objects.all(), 'patients': Patient.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AppointmentEdit(UpdateView):
    model = Appointment
    fields = '__all__'
    template_name = 'poly/appointment/edit.html'
    success_url = reverse_lazy('poly:appointment-list')
    extra_context = {'doctors': Doctor.objects.all(), 'patients': Patient.objects.all()}


def appointment_delete(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if appointment.delete():
        return redirect('/appointment/list')


class AppointmentCreate(CreateView):
    model = Appointment
    template_name = 'poly/appointment/add.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('poly:appointment-list')
    extra_context = {'doctors': Doctor.objects.all(), 'patients': Patient.objects.all()}

    def form_valid(self, form):
        return super(AppointmentCreate, self).form_valid(form)

