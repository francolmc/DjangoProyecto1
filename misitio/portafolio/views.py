from django.shortcuts import render

# Create your views here.
def portafolio_home(request):
    return render(request, 'portafolio_home.html')