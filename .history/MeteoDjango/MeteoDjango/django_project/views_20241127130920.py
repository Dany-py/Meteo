from django.shortcuts import render
Response

def home(request):
    return render(request, 'home.html')