from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"index.html")

    #return HttpResponse("<h1>hello this is my first webpage.<h1>")
