from django.forms import ModelForm

from poly.models import Doctor


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
