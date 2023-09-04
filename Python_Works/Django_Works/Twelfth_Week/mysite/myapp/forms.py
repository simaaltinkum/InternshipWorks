from django.forms import ModelForm
from myapp.models import Tweet

class TweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["content", "image"]
