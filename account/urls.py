from django.urls import path

from account import views

urlpatterns = [

    path('', views.home, name='home'),
    path('update/', views.update, name='update')
]