from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy

from poly.forms.treatment import TreatmentForm
from poly.models import Treatment, Clinic, Appointment, Doctor, Patient


def treatment_json(request):
    data = []
    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))
    items = Treatment.objects.all()
    records_total = items.count()
    items = items[start:length]
    records_filtered = items.count()
    for item in items:
        data.append([
            item.doctor.name + ' ' + item.doctor.surname,
            item.patient.name + ' ' + item.patient.surname,
            item.date,
            '<a href="/treatment/detail/' + str(item.id) + '" class="btn btn-primary btn-xs"><i class="fa fa-folder">'
            '</i> Görüntüle</a>'
            '<a href="/treatment/edit/' + str(item.id) + '" class="btn btn-info btn-xs">'
            '<i class="fa fa-pencil"></i> Düzenle </a>'
            '<a href="/treatment/delete/' + str(item.id) + '" class="btn btn-danger btn-xs">'
            '<i class="fa fa-trash-o"></i> Sil </a>'
        ])
    return JsonResponse({
        'recordsTotal': records_total,
        'recordsFiltered': records_filtered,
        'data': data
    }, safe=False)


class TreatmentList(ListView):
    template_name = 'poly/treatment/list.html'
    context_object_name = 'treatment_list'

    def get_queryset(self):
        if self.request.is_ajax():
            return JsonResponse(list(Treatment.objects.all().values('id_number', 'name', 'surname', )), safe=False)
        return None


class TreatmentDetail(DetailView):
    model = Treatment
    template_name = 'poly/treatment/detail.html'
    extra_context = {'clinics': Clinic.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TreatmentEdit(UpdateView):
    model = Treatment
    fields = '__all__'
    template_name = 'poly/treatment/edit.html'
    success_url = reverse_lazy('poly:treatment-list')
    extra_context = {'clinics': Clinic.objects.all()}


def treatment_delete(request, pk):
    treatment = Treatment.objects.get(pk=pk)
    if treatment.delete():
        return redirect('/treatment/list')


def treatment_create(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'poly/treatment/add.html', {
                          'doctor': appointment.doctor,
                          'patient': appointment.patient
                      })
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = Treatment(
                doctor=form.cleaned_data['doctor'],
                patient=form.cleaned_data['patient'],
                diagnosis=form.cleaned_data['diagnosis'],
            )
            treatment.save()
        return reverse_lazy('poly:treatment-list')

#
# class TreatmentCreate(CreateView):
#     model = Treatment
#     template_name = 'poly/treatment/add.html'
#     form_class = TreatmentForm
#     success_url = reverse_lazy('poly:treatment-list')
#     extra_context = {'clinics': Clinic.objects.all()}
#
#     def form_valid(self, form):
#         return super(TreatmentCreate, self).form_valid(form)
#
