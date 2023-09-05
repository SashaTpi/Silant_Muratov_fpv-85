from django import forms
from .models import Mashins, TO, Reclamation


class FormReclamation(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__'


class FormCar(forms.ModelForm):
    class Meta:
        model = Mashins
        fields = '__all__'


class FormRepSer(forms.ModelForm):
    class Meta:
        model = TO
        fields = '__all__'
        widgets = {
            'vid_TO': forms.RadioSelect()
        }


