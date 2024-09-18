from django.shortcuts import render

# Create your views here.

def accueil(request):
  return render(request, 'Accueil.html')
  
def about(request):
  return render(request, 'About.html')

def contact(request):
  return render(request, 'Contact.html')