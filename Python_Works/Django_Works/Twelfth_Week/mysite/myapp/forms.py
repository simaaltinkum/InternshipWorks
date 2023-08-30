from django.forms import ModelForm
from myapp.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['user_name', 'email', 'password']