from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})

@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
            article.title = request.POST.get('title', article.title)
            article.content = request.POST.get('content', article.content)
            article.save()
            return redirect('dashboard')
    
    return render(request, 'blog/edit_article.html', {'article': article})

def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('dashboard')


@login_required
def dashboard(request):
    articles = Article.objects.all()
    return render(request, 'blog/dashboard.html', {'articles': articles})
