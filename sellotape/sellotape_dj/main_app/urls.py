from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/<str:username>/', views.feed, name='feed'),
]
