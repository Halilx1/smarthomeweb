from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   #return HttpResponse("Hallo aus der Gui-Seite")
    return render(request, 'gui\index_start.html')