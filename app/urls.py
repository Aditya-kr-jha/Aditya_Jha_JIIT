from django.urls import path

from app import views


urlpatterns = [
    path('',views.home,name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),
]