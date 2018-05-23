from django.forms import ModelForm

from poly.models import Clinic


class ClinicForm(ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'
