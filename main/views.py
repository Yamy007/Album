from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import Article, Customer, Status, Sex
# Create your views here.


def users(request: object):
    return redirect("/customer")


def customer(request: object):
    if request.methods == "POST":
        customer = Customer()
        customer.user = request.user
        customer.age = request.POST.get("age")
        customer.sex = request.POST.get("sex")
        customer.part = request.POST.get("part")
        customer.born = request.POST.get("born")
        customer.nickname = request.POST.get("nickname")
        customer.status = request.POST.get("status")
        customer.save()
        return redirect("/")
    else:
        status = Status.objects.all()
        sex = Sex.objects.all()
        return render(request, "main/customer.html", {"status":status, "sex": sex})


def index(request: object):
    customer = Customer.objects.filter(user = request.user)
    if customer:
            
        if request.user.is_authenticated:
            article = Article.objects.filter(owner = request.user )
            return render(request, "main/index.html", {"article": article})
        else:
            return redirect('/users/login')    
    else:
        return redirect("/customer")
    
def articles(request: object):
    if request.methods == "POST":
        if form.is_valid:
            pass
        else:
            return render(request, "main/article.html")    
        
    else:
        return render(request, "main/article.html")