from django.urls import path
from . import views

urlpatterns=[
    path('education/', views.education, name='education'),
    path('documents/', views.add_documents, name='documents'),
    path('work/', views.work_experience, name="work"),
]