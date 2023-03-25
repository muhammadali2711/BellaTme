from django import forms

from bmain.models import AboutCourse


class RootForm(forms.ModelForm):
    class Meta:
        model = AboutCourse
        fields = '__all__'
