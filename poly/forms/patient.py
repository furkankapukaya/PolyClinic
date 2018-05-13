from django import forms

from poly.models import Patient


class PatientFrom(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

