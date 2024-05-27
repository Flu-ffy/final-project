from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def education(request):
    return render(request, 'modules/education.html')

def add_documents(request):
    return render(request, 'modules/add_documents.html')
