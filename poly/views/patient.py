from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy

from poly.forms.patient import PatientFrom
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
            item.code,
            item.name,
            '<a href="#" class="btn btn-primary btn-xs"><i class="fa fa-folder">'
            '</i> Görüntüle </a><a href="#" class="btn btn-info btn-xs">'
            '<i class="fa fa-pencil"></i> Düzenle </a>'
            '<a href="{% url "web:patient-delete "' + str(item.id) + ' %}" class="btn btn-danger btn-xs">'
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
            return JsonResponse(list(Patient.objects.all().values('code', 'name')), safe=False)
        return None


class PatientCreate(CreateView):
    model = Patient
    template_name = 'poly/patient/add.html'
    form_class = PatientFrom
    success_url = reverse_lazy('poly:patient-list')

    def form_valid(self, form):
        return super(PatientCreate, self).form_valid(form)


class PatientDelete(DeleteView):
    model = Patient
    template_name = 'poly/patient/patient_confirm_delete.html'
    success_url = reverse_lazy('poly:patient-list')