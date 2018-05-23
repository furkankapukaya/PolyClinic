from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy

from poly.forms.doctor import DoctorForm
from poly.models import Doctor, Clinic


def doctor_json(request):
    data = []
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    items = Doctor.objects.all()
    records_total = items.count()
    items = items[start:length]
    records_filtered = items.count()
    for item in items:
        data.append([
            item.id_number,
            item.name,
            item.surname,
            item.clinic.name,
            '<a href="/doctor/detail/' + str(item.id) + '" class="btn btn-primary btn-xs"><i class="fa fa-folder">'
            '</i> Görüntüle</a>'
            '<a href="/doctor/edit/' + str(item.id) + '" class="btn btn-info btn-xs">'
            '<i class="fa fa-pencil"></i> Düzenle </a>'
            '<a href="/doctor/delete/' + str(item.id) + '" class="btn btn-danger btn-xs">'
            '<i class="fa fa-trash-o"></i> Sil </a>'
        ])
    return JsonResponse({
        'recordsTotal': records_total,
        'recordsFiltered': records_filtered,
        'data': data
    }, safe=False)


class DoctorList(ListView):
    template_name = 'poly/doctor/list.html'
    context_object_name = 'doctor_list'

    def get_queryset(self):
        if self.request.is_ajax():
            return JsonResponse(list(Doctor.objects.all().values('id_number', 'name', 'surname', 'clinic__doctor__name')), safe=False)
        return None


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'poly/doctor/detail.html'
    extra_context = {'clinics': Clinic.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DoctorEdit(UpdateView):
    model = Doctor
    fields = '__all__'
    template_name = 'poly/doctor/edit.html'
    success_url = reverse_lazy('poly:doctor-list')
    extra_context = {'clinics': Clinic.objects.all()}


def doctor_delete(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if doctor.delete():
        return redirect('/doctor/list')


class DoctorCreate(CreateView):
    model = Doctor
    template_name = 'poly/doctor/add.html'
    form_class = DoctorForm
    success_url = reverse_lazy('poly:doctor-list')
    extra_context = {'clinics': Clinic.objects.all()}

    def form_valid(self, form):
        return super(DoctorCreate, self).form_valid(form)

