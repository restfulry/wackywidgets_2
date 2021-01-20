from django.shortcuts import render
from django.http import HttpResponse
from .models import Widget
from .forms import WidgetForm


def home_index(request):
    widget_list = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widget_list': widget_list, 'widget_form': widget_form})
