from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.ilogin,name='users-login'),
    path('register/',views.iregister,name='users-register')
]