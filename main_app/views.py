from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Widget
from .forms import WidgetForm


def home_index(request):
    widget_list = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widget_list': widget_list, 'widget_form': widget_form})


def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home_index')


def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('home_index')
