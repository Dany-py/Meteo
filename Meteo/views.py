from django.shortcuts import render
from .models import CodeInse, Message
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json

# Create your views here.

def accueil(request):
  return render(request, 'Accueil.html')
  
def about(request):
  return render(request, 'About.html')

def contact(request):
  return render(request, 'Contact.html')

# Views for finding town's code
@csrf_exempt
def find_code(request):
  if request.method ==  'POST':
      data =  json.loads(request.body)
      the_town = data.get('town')

      #Analyse
      if CodeInse.objects.filter(town = the_town).exists():
        town_code = CodeInse.objects.get(town = the_town).code
      else:
        town_code = "Code not found"
      return JsonResponse({'code':town_code})
  else:
      return JsonResponse({'error':'Invalide request'}, status =400)
  
#View for call api Meteo Concept
@csrf_exempt
def api_request_view(request):
     if request.method == 'POST':
        code = find_code(request)

        the_code = json.loads(code.content)
        code_string = str(the_code["code"])

        if len(code_string) >5:
           return  JsonResponse({"message": "Aucune information trovée pour la ville saisie"})
        else:
           api_url = "https://api.meteo-concept.com/api/forecast/daily/0?token=36ef80f9b9c5e2310d624239d73726c34673d397cf14101abb5c1e8239ce23f4&insee=" + code_string

           response = requests.get(api_url)

           if response.status_code == 200:
              api_data =  response.json()
              city = api_data.get('city')
              weather =  api_data.get('forecast')
              text = "Votre ville " + city.get('name') + " a, pour la journée d'aujourd'hui, " + str(weather.get('probafog'))  + "pourcentage de risque de brouillard, " + str(weather.get('probafrost')) + " pourcentage de risque de neige, " + str(weather.get('probarain')) + " pourcentage de risque de pluie."
              return JsonResponse({"message": text})
           else:
              return JsonResponse({"message":"Erreur lors de l'appel api" })
            
 
#View for send message on contact page
@csrf_exempt
def send_contact_message(request):
    if request.method == 'POST':
      data =  json.loads(request.body)
      Message.objects.create(email = data.get('email'), message = data.get('message'))
      return JsonResponse({"message": "Successful sent"})
    else:
      return JsonResponse({"message": "Unsuccessful sent"})