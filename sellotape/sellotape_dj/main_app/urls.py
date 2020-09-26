from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-stream/', views.add_stream, name='add_stream'),
]
