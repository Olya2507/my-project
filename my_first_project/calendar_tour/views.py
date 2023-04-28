from django.http import HttpResponse
from django.shortcuts import render


def calendar_tour(request):
    return render(request, 'calendar_tour.html')


