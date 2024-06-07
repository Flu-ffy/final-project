from django.urls import path
from . import views

urlpatterns=[
    path('personal/',views.personal,name='modules-personal'),
    path('faqs/',views.faqs,name='modules-faqs'),
    path('error_page/',views.error_page,name='modules-error_page'),
     path('questions/',views.questions_view,name='modules-questions'),
]
    