from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.dateparse import parse_date

from .models import Article, Category, SubCategory


def list(request):
    date = request.GET.get('date')
    if date is None:
        date = datetime.now().date()
    else:
        date = parse_date(date)

    articles = Article.objects.filter(UploadDate=date)
    categories = Category.objects.all()

    top5Articles = Article.objects.all().order_by('-Views')[:5]
    return render(request, "index.html",
                  {"articles": articles, "categories": categories, "date": str(date), "top5Articles": top5Articles})


def view(request, id):
    article = Article.objects.get(Id=id)
    if article is None:
        return render(request, "404.html")
    article.Views += 1
    article.save()
    return render(request, "view.html", {"article": article})


def getSubCategories(request):
    catagoryId = int(request.GET.get('id'))
    category = Category.objects.get(Id=catagoryId)
    subCategories = SubCategory.objects.filter(Category=category)
    sub = {}
    for subCategory in subCategories:
        sub[subCategory.Id] = subCategory.Name
    return JsonResponse(sub)


def geCategories(request):
    categories = Category.objects.all()
    cat = {}
    for cate in categories:
        cat[cate.Id] = cate.Name
    return JsonResponse(cat)


def getArticlesBySubCategories(request, id):
    subCategory = SubCategory.objects.get(Id=id)
    if subCategory is None:
        return render(request, "404.html")
    page = request.GET.get('page')

    articles_list = Article.objects.filter(SubCategory=subCategory)
    paginator = Paginator(articles_list, 12)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, "subcategory.html", {"subcategory": subCategory, "articles": articles})
