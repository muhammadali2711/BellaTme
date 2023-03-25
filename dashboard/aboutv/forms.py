from django import forms

from bmain.models import AboutVacancy


class RootForm(forms.ModelForm):
    class Meta:
        model = AboutVacancy
        fields = '__all__'
