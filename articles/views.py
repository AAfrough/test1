from django.shortcuts import render , redirect
from django.shortcuts import HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def articles_list(request):
    articles = models.Articles.objects.all().order_by("-date")
    args = {'articles': articles}
    return render(request , "articles/articles_list.html" , args)

def article_detaile(request , slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.get(slug=slug)
    return render(request , "articles/article_detaile.html" , {'article' : article})


@login_required(login_url= "/accounts/login")#agar login nabashe vared in safe beshe# ba in kar decorator bar roye in tabe ziri emal mishavad
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST , request.FILES)
        if form.is_valid():
            instance = form.save(commit=False )
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request , 'articles/create_article.html' , {'form' : form})