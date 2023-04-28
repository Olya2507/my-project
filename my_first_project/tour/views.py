from .models import Tour
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def tour(request):
    return render(request, 'tours.html')

def tour_1(request):
    return render(request, 'tour_program.html')

def tour_2(request):
    return render(request, 'tour_program2.html')

def tour_3(request):
    return render(request, 'tour_program3.html')

def tour_4(request):
    return render(request, 'tour_program4.html')

def tour_5(request):
    return render(request, 'tour_program5.html')

# создаем экземпляр класса пагинатор с количеством объектов, которые должны отображаться на каждой странице.
def tour_index(request):
    tours = Tour.objects.all()
    paginator = Paginator(tours, 4)  # 4 тура на странице
    # получаем параметр GET, который указывает номер текущей страницы.
    page = request.GET.get('page')
    try:
        tours = paginator.page(page)  # получаем объекты для требуемой страницы, вызывающей page() метод Paginator
    except PageNotAnInteger:
        # Если параметр страницы не является целым числом, мы извлекаем первую страницу результатов.
        tours = paginator.page(1)
    except EmptyPage:
        # Если этот параметр является числом, превышающим последнюю страницу результатов, мы извлекаем последнюю страницу.
        tours = paginator.page(paginator.num_pages)
        # возвращаем страницы соответствии с указанным шаблоном
    return render(request,
                  'tour_index.html',
                  {'page': page,
                   'tours': tours})



def tour_detail(request, pk):
    tour = Tour.objects.get(pk=pk)
    context = {
        'tour': tour
    }
    return render(request, 'tour_detail.html', context)

