from django.forms import ModelForm
from qr_app.models import Qr

class TweetModelForm(ModelForm):
    class Meta:
        model = Qr
        fields = ['qr']