from django.forms import ModelForm
from qr_app.models import Qr

class QrForm(ModelForm):
    class Meta:
        model = Qr
        fields = ['type']

class QrSavingForm(ModelForm):

    class Meta:
        model = Qr
        fields = ['qr', 'image', 'type']