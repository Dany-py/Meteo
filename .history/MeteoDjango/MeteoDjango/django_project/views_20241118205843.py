from django.shortcuts import render
from django.http import HttpResponse

def base_page (request):
    return HttpResponse("")
    return render(request, 'base.html')