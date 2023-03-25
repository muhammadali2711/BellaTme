from django import forms

from bmain.models import Why


class RootForm(forms.ModelForm):
    class Meta:
        model = Why
        fields = '__all__'
