from django import forms

from bmain.models import Sifat


class RootForm(forms.ModelForm):
    class Meta:
        model = Sifat
        fields = '__all__'
