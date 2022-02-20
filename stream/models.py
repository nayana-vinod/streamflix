from operator import mod
from django.db import models

from django.contrib.auth.models import AbstractUser

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


class UserDetails(models.Model):
    name = models.TextField(max_length=30, null=True)
    email = models.EmailField(max_length=30, null=True, unique=True)
    bio = models.TextField(null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
    phno = models.IntegerField(null=True, unique=True)
    age = models.IntegerField(null=True, blank=True)

    # avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS =[]

    def __str__(self):
        return str(self.email)


class User(models.Model):
    email = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.email)
