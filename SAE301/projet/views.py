from django.shortcuts import render

# Create your views here.

def bonjour(request):
    return render(request, "projet/bonjour.html")