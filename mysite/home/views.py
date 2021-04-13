from django.shortcuts import render, HttpResponse
from .models import home_page

# Create your views here.
def index(request):

    home_page_values = home_page.objects.all()

    return render(request, 'home.html', {"home": home_page_values})
