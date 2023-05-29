from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#  Create your views here.
def index(request):
    from django.conf import settings

    print(settings.CONFIG_LOAD) # custom variable
        
    return HttpResponse("Bienvenidos al app base")