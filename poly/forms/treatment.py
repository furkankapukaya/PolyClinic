from django.forms import ModelForm, forms

from poly.models import Treatment


class TreatmentForm(forms.Form):
    class Meta:
        model = Treatment
        fields = '__all__'
