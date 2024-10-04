from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
]
