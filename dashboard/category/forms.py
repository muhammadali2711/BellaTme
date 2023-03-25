from django import forms

from bmain.models import Category


class CtgForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
