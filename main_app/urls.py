from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('add/', views.add_widget, name='add_widget'),
    path('widget/<int:widget_id>/delete/',
         views.delete_widget, name='delete_widget'),
]
