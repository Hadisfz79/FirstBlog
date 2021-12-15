from django.shortcuts import render
from . import models

# Create your views here.
def article(request):
    articles = models.Article.objects.all().order_by('date')
    args = {'articles' : articles}
    return render(request,'article/article.html' , args)
