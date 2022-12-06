from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Article
# Create your views here.


def users(request):
    return redirect("/")


def index(request: object):
    if request.user.is_authenticated:
        article = Article.object.filter(owner = request.user)
        return render(request, "main/index.html", {"article": article})
        
    else:
        redirect('/users/login')