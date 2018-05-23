from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy

from poly.forms.patient import PatientForm
from poly.models import Patient


def patient_json(request):
    data = []
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    items = Patient.objects.all()
    records_total = items.count()
    items = items[start:length]
    records_filtered = items.count()
    for item in items:
        data.append([
            item.id_number,
            item.name,
            item.surname,
            '<a href="/patient/detail/' + str(item.id) + '" class="btn btn-primary btn-xs"><i class="fa fa-folder">'
            '</i> Görüntüle</a>'
            '<a href="/patient/edit/' + str(item.id) + '" class="btn btn-info btn-xs">'
            '<i class="fa fa-pencil"></i> Düzenle </a>'
            '<a href="/patient/delete/' + str(item.id) + '" class="btn btn-danger btn-xs">'
            '<i class="fa fa-trash-o"></i> Sil </a>'
        ])
    return JsonResponse({
        'recordsTotal': records_total,
        'recordsFiltered': records_filtered,
        'data': data
    }, safe=False)


class PatientList(ListView):
    template_name = 'poly/patient/list.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        if self.request.is_ajax():
            return JsonResponse(list(Patient.objects.all().values('id_number', 'name', 'surname')), safe=False)
        return None


class PatientDetail(DetailView):
    model = Patient
    template_name = 'poly/patient/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PatientEdit(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'poly/patient/edit.html'
    success_url = reverse_lazy('poly:patient-list')


def patient_delete(request, pk):
    patient = Patient.objects.get(pk=pk)
    if patient.delete():
        return redirect('/patient/list')


class PatientCreate(CreateView):
    model = Patient
    template_name = 'poly/patient/add.html'
    form_class = PatientForm
    success_url = reverse_lazy('poly:patient-list')

    def form_valid(self, form):
        return super(PatientCreate, self).form_valid(form)

