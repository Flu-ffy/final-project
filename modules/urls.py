from django.urls import path
from . import views

urlpatterns=[
    path('personal/',views.personal,name='modules-personal'),
    path('faqs/',views.faqs,name='modules-faqs'),
    path('error/',views.error_view,name='error'),
]
    