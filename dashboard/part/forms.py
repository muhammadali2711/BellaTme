from django import forms

from bmain.models import Partner


class RootForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
