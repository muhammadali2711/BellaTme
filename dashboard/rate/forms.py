from django import forms

from bmain.models import Rating


class RootForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
