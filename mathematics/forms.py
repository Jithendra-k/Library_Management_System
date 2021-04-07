from django import forms
from django.forms import ModelForm
from .models import Maths


class MathematicsForm(ModelForm):
    class Meta:
        model = Maths
        fields = ['m_name', 'm_year']
