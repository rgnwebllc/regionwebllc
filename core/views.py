from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'core/home.html', {'year': datetime.now().year})