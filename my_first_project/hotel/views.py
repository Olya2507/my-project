from .models import Hotel
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# def hotel(request):
#     return render(request, 'hotel.html')

def hotel_index(request):
    hotels = Hotel.objects.all()
    paginator = Paginator(hotels, 4)  # 4 тура на странице
    # получаем параметр GET, который указывает номер текущей страницы.
    page = request.GET.get('page')
    try:
        hotels = paginator.page(page)  # получаем объекты для требуемой страницы, вызывающей page() метод Paginator
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом, мы извлекаем первую страницу результатов.
        hotels = paginator.page(1)
    except EmptyPage:
        # Если этот параметр является числом, превышающим последнюю страницу результатов, мы извлекаем последнюю страницу.
        hotels = paginator.page(paginator.num_pages)
        # возвращаем страницы соответствии с указанным шаблоном
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
