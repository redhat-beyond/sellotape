from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('<str:username>/', views.user, name='user'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
]
