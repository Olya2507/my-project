from .models import Hotel
from django.shortcuts import render

# def hotel(request):
#     return render(request, 'hotel.html')

def hotel_index(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel_index.html', context)

def hotel_detail(request, pk):
    hotel = Hotel.objects.get(pk=pk)
    context = {
        'hotel': hotel
    }
    return render(request, 'hotel_detail.html', context)
