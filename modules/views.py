from django.shortcuts import render
from django .views import View
from .models import FAQ


def faqs(request):
    faqs = FAQ.objects.all()
def error_view(request):
    return render(request, 'error.html')

def personal(request):
    if request.method == 'POST':
        # Handle form submission logic here
        if 'proceed' in request.POST:
            # Logic for proceeding, possibly validation, etc.
            return render(request, 'error.html')
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
        return render(request, '/modules/personal.html', context)
        



