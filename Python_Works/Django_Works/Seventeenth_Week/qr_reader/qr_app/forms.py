from django.forms import ModelForm
from django import forms
from qr_app.models import Qr

class QrForm(ModelForm):
    pk = forms.CharField()
    class Meta:
        model = Qr
        fields = ['type', 'pk']