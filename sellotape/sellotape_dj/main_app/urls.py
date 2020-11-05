from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('add-stream/', views.add_stream, name='add_stream'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('<str:username>/', views.user, name='user'),
]
