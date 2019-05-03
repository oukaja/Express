from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from main.models import Articles

# def home(request):
#     numbers_list = range(1, Articles.objects().count())
#     page = request.GET.get('page', 1)
#     paginator = Paginator(numbers_list, 20)
#     try:
#         numbers = paginator.page(page)
#     except PageNotAnInteger:
#         numbers = paginator.page(1)
#     except EmptyPage:
#         numbers = paginator.page(paginator.num_pages)
#     return render(request, 'home.html', {'numbers': numbers})

def home(request):
    articles = Articles.objects()
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 10)
    try:
        sarticles = paginator.page(page)
    except PageNotAnInteger:
        sarticles = paginator.page(1)
    except EmptyPage:
        sarticles = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'sarticles': sarticles})


