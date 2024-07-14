from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.app, name='app'),
  path('<str:country_name>/', views.country_detail, name='country_detail'),
]

