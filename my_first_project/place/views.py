from django.http import HttpResponse
from django.shortcuts import render

def place(request):
    return render(request, 'place.html')


# Create your views here.
