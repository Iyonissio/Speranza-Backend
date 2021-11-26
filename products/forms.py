from django import forms
from django.forms.models import inlineformset_factory
from .models import Condutor, Viatura, Chapa

class CondutorForm(forms.ModelForm):
    class Meta:
        model = Condutor
        fields = '__all__'

class ViaturaForm(forms.ModelForm):
    class Meta:
        model = Viatura
        fields = '__all__'

class ChapaForm(forms.ModelForm):
    class Meta:
        model = Chapa
        fields = '__all__'

