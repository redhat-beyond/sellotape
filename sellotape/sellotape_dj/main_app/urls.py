from django.urls import path

from . import views

urlpatterns = [
    path('complete-login/', views.complete_login, name='complete-login'),
    path('', views.landing, name='landing'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('<str:username>/', views.user, name='user'),
]
