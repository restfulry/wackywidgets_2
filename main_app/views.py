from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum


def home_index(request):
    widget_list = Widget.objects.all()
    widget_form = WidgetForm()
    total_quantity = Widget.objects.aggregate(Sum('quantity'))['quantity__sum']
    return render(request, 'index.html', {'widget_list': widget_list, 'widget_form': widget_form, 'total_quantity': total_quantity})


def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home_index')


def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('home_index')
