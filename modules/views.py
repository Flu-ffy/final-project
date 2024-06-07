from django.shortcuts import render
from django .views import View
from .models import FAQ


def faqs(request):
    faqs = FAQ.objects.all()
def error_page(request):
    return render(request, 'error_page.html')

def personal(request):
    if request.method == 'POST':
        # Handle form submission logic here
        if 'proceed' in request.POST:
            # Logic for proceeding, possibly validation, etc.
            return render(request, 'error_page.html')
        elif 'saved' in request.POST:
            # Logic for saving form data
            # You can handle saving data to the database here
            pass

    return render(request, 'personal.html')
def personal(request):
    return render(request, 'modules/personal.html')
class PersonalView(View):
    def get(self, request):
        context = {}
        return render(request, 'modules/personal.html', context)
    
def questions_view(request):
    questions = [
        {
            'id': 1,
            'question': 'What is the capital of France?',
            'choices': ['Paris', 'London', 'Berlin', 'Rome']
        },
        {
            'id': 2,
            'question': 'What is the capital of Japan?',
            'choices': ['Tokyo', 'Seoul', 'Beijing', 'Osaka']
        },
        {
            'id': 3,
            'question': 'What is 2 + 2?',
            'input': True
        },
        # Add more questions here
    ]
    return render(request, 'modules/questions.html', {'questions': questions})
    
        



