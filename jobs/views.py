from django.shortcuts import render
from .models import assignment
# Create your views here.
def home(request):
    test = assignment.objects
    return render(request, 'jobs/home.html', {'jobs': test})