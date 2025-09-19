from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    path('get_product/', views.get_product)
]
