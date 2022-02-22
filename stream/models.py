from operator import mod
from turtle import mode
from django.db import models

# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Production(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    # created = models.DateField(auto_now_add=False, null=True)
    created = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=200, null=True)
    description =  models.TextField(null=True, blank=True)
    production = models.ManyToManyField(Production, blank=True)
    # created = models.DateField(auto_now_add=False)
    released = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-released']
    
    def __str__(self):
        return self.name 

class Plan(models.Model):
    name = models.CharField(max_length=200, null=True)
    description =  models.TextField(null=True, blank=True)
    price = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name 

class Watchlist(models.Model):
    # host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shows = models.ManyToManyField(Show)

    def __str__(self):
       return f"{self.user}'s WatchList"


# class UserDetails(models.Model):
#     email = models.EmailField(null=True, unique=True)
#     name = models.CharField(max_length=30, null=True)
#     bio = models.TextField(null=True, blank=True)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
#     phno = models.IntegerField(null=True, unique=True)
#     age = models.IntegerField(null=True, blank=True)

#     # avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS =[]

#     def __str__(self):
#         return str(self.email)


# class User(models.Model):
# #     email_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True)
#     # email = models.EmailField(max_length=30, null=True, unique=True) 

#     email = models.OneToOneField(UserDetails, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return str(self.email)
