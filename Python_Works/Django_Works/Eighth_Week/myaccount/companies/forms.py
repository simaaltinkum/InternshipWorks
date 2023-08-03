from django import forms
from django.forms import ModelForm

from companies.models import Companies, Operation


class CompaniesForm(ModelForm):
    class Meta:
        model = Companies
        fields = ["company_name", "boss_name", "email", "telephone", "tax"]

class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ["debt", "credit"]

# class CompaniesForm(forms.Form):
#     company_name = forms.CharField(max_length=200)
#     boss_name = forms.CharField(max_length=200)
#     debt = forms.IntegerField()
#     credit = forms.IntegerField()

"""class CustomerForm(forms.Form):
    name = forms.CharField(max_length=200)
    debt = forms.IntegerField()
    credit = forms.IntegerField() """
