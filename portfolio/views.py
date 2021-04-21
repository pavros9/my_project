from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Article
from django.views.generic import DetailView
from django.views.generic.base import View

from .forms import QuizForm

from django.core.paginator import Paginator

def index(request):

    # Если данный запрос типа POST
    if request.method == "POST":
        form = QuizForm(request.POST)
        # Проверка валидности формы
        if form.is_valid():
            form.clean_rating()
            form.save()
            return redirect ('/')
        return render(request, 'portfolio/index.html', {'form': form})

    form = QuizForm()

    data = {
        'form': form,
    }
    return render(request, 'portfolio/index.html', data)

def projects(request):
    return render(request, 'portfolio/projects.html')

def aboutme(request):
    article = Article.objects.all()
    return render(request, 'portfolio/aboutme.html', {'article': article})

def aboutsite(request):
    #сортировка по дате(убывание)
    posts = Post.objects.order_by('-created_date')

    #пагинация  - порядковая нумерация страниц
    paginator = Paginator(posts, 4)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else: 
        prev_url=''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }

    return render(request, 'portfolio/aboutsite.html', context = context)

class AboutSiteDetailView(DetailView):
    model = Post
    template_name = 'portfolio/details_view.html'
    context_object_name = 'post'

class AboutMeDetailView(DetailView):
    model = Article
    template_name = 'portfolio/aboutme.html'
    context_object_name = 'article'


def game(request):
    return render(request, 'portfolio/game.html')