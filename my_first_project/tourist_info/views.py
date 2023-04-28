from django.http import HttpResponse
from django.shortcuts import render

def tourist_info(request):
    return render(request, 'tourist_info.html')

def payment(request):
    return render(request, 'payment.html')

def sale(request):
    return render(request, 'sale.html')



# Create your views here.
