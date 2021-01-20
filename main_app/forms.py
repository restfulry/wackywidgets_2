from django import forms
from django.forms import ModelForm
from .models import Widget


class WidgetForm(forms.ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
