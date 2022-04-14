from operator import mod
from turtle import mode
from django.db import models

# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Production(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    # show = models.ForeignKey(Show, on_delete=models.SET_NULL, null=True, blank=True)
    # created = models.DateField(auto_now_add=False, null=True)
    created = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Show(models.Model):
    name = models.CharField(max_length=200, null=True)
    description =  models.TextField(null=True, blank=True)
    # production = models.ManyToManyField(Production, blank=True)
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, null=True, blank=True)
    # created = models.DateField(auto_now_add=False)
    released = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-released']
    
    def __str__(self):
        return self.name 
    
# class Production(models.Model):
#     name = models.CharField(max_length=200)
#     description =  models.TextField(null=True, blank=True)
#     show = models.ForeignKey(Show, on_delete=models.SET_NULL, null=True, blank=True)
#     # created = models.DateField(auto_now_add=False, null=True)
#     created = models.IntegerField(null=True, blank=True)

#     def __str__(self):
#         return self.name

class Watchlist(models.Model):
    # host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # show = models.ForeignKey(Show, on_delete=models.SET_NULL, null=True)
    show = models.ManyToManyField(Show)

    def __str__(self):
       return f"{self.user}'s WatchList"
        # return self.user

    