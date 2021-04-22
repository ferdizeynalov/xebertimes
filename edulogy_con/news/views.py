from django.shortcuts import render
from . models import News, Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def news_list(request):
    newses = News.objects.all().order_by('-date')
    categories = Category.objects.all()[:10]
    paginator = Paginator(newses, 15) # Show 15 news per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories':categories,
        'newses':page_obj,
    }
    return render(request, 'news.html', context)


def news_detail(request, category_slug, news_id):
    news = News.objects.get(category__slug=category_slug,id=news_id)
    categories = Category.objects.all()
    context = {
        'news':news,
        'categories':categories,
    }
    return render(request, 'news-single.html', context)

def news_by_category(request, category_slug):
    newses = News.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    context = {
        'newses':newses,
        'categories':categories,
    }
    return render(request, 'news.html', context)

def search(request):
    newses = News.objects.filter(Q(name__contains=request.GET['search']) | Q(description__contains=request.GET['search']))
    categories = Category.objects.all()

    context = {
        'newses': newses,
        'categories': categories,
    }

    return render(request, 'news.html', context)
