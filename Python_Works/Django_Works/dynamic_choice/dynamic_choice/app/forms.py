from django import forms
from .models import Category, SubCategory, Saved
from django.forms import ModelForm


class MyForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.none())

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = SubCategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass


class SaveForm(ModelForm):
    class Meta:
        model = Saved
        fields = ['selected_datetime', 'category', 'subcategory']