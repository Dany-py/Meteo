from django.shortcuts import render
om django.http import HttpResponse

def home(request):
    return render(request, 'home.html')