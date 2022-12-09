from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Status(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title


class Sex(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    age = models.IntegerField(default=18)
    sex = models.ForeignKey(Sex, on_delete = models.CASCADE)
    part = models.CharField(max_length=255) #boyfriend or girlfriend only username 
    born = models.DateField()
    nickname = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    def __str__(self):
        return self.nickname


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Date(models.Model):
    boy = models.CharField(max_length=255)  #Customer
    girl = models.CharField(max_length=255) #Customer
    start_date = models.DateField()
    def __str__(self):
        return self.boy
    
    
class Commentary(models.Model):
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.owner
    
    
class Calendar(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event = models.DateTimeField()
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.description
    
    