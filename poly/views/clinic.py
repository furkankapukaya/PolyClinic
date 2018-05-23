from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy

from poly.forms.clinic import ClinicForm
from poly.models import Clinic, Polyclinic


def clinic_json(request):
    data = []
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    items = Clinic.objects.all()
    records_total = items.count()
    items = items[start:length]
    records_filtered = items.count()
    for item in items:
        data.append([
            item.id,
            item.name,
            '<a href="/clinic/detail/' + str(item.id) + '" class="btn btn-primary btn-xs"><i class="fa fa-folder">'
            '</i> Görüntüle</a>'
            '<a href="/clinic/edit/' + str(item.id) + '" class="btn btn-info btn-xs">'
            '<i class="fa fa-pencil"></i> Düzenle </a>'
            '<a href="/clinic/delete/' + str(item.id) + '" class="btn btn-danger btn-xs">'
            '<i class="fa fa-trash-o"></i> Sil </a>'
        ])
    return JsonResponse({
        'recordsTotal': records_total,
        'recordsFiltered': records_filtered,
        'data': data
    }, safe=False)


class ClinicList(ListView):
    template_name = 'poly/clinic/list.html'
    context_object_name = 'clinic_list'

    def get_queryset(self):
        if self.request.is_ajax():
            return JsonResponse(list(Clinic.objects.all().values('id_number', 'name')), safe=False)
        return None


class ClinicDetail(DetailView):
    model = Clinic
    template_name = 'poly/clinic/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClinicEdit(UpdateView):
    model = Clinic
    fields = '__all__'
    template_name = 'poly/clinic/edit.html'
    success_url = reverse_lazy('poly:clinic-list')
    extra_context = {'polyclinics': Polyclinic.objects.all()}



def clinic_delete(request, pk):
    clinic = Clinic.objects.get(pk=pk)
    if clinic.delete():
        return redirect('/clinic/list')


class ClinicCreate(CreateView):
    model = Clinic
    template_name = 'poly/clinic/add.html'
    form_class = ClinicForm
    success_url = reverse_lazy('poly:clinic-list')
    extra_context = {'polyclinics': Polyclinic.objects.all()}

    def form_valid(self, form):
        return super(ClinicCreate, self).form_valid(form)

