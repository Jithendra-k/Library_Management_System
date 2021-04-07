from django import forms
from django.forms import ModelForm
from .models import Biology


class BiologyForm(ModelForm):
    class Meta:
        model = Biology
        fields = ['b_name', 'b_year']
