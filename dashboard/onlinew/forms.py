from django import forms

from bmain.models import OnlineWork


class RootForm(forms.ModelForm):
    class Meta:
        model = OnlineWork
        fields = '__all__'
