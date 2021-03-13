from django.shortcuts import render

from .models import Article


def list(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})


def view(request, id):
    article = Article.objects.get(Id=id)
    article.Views += 1
    article.save()
    return render(request, "view.html", {"article": article})
