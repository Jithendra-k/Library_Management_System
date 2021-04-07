from django import forms
from django.forms import ModelForm
from .models import OOPS


class OOPSForm(ModelForm):
    class Meta:
        model = OOPS
        fields = ['o_name', 'o_year']
