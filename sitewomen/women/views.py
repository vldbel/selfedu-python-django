from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request): # HTTPrequest
    return HttpResponse("Страница")

def categories(request, cat_id): # HTTPrequest
    return HttpResponse(f"<h1>Категории</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug): # HTTPrequest
    return HttpResponse(f"<h1>Категории</h1><p>slug: {cat_slug}</p>")

def archive(request, year): # HTTPrequest
    return HttpResponse(f"<h1>Архив по годам</h1><p>slug: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not Found</h1>')