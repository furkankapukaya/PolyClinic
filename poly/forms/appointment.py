from django.forms import ModelForm

from poly.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
