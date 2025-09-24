from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login', views.user_login, name='user-login'),
    path('signup', views.user_signup, name='user_signup'),
]
