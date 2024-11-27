from django.shortcuts import render
nse

def home(request):
    return render(request, 'home.html')