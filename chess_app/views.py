from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")
    
def chess_stats(request):
    return HttpResponse("What time are the stats coming?")

def index(request):
    return HttpResponse("Hello, world. You're at the index.")