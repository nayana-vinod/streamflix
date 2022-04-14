from multiprocessing import context
from django.shortcuts import render, redirect
# from django.http import request, HttpResponse
from .models import Show, Production, Watchlist
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.forms import UserCreationForm
# from .forms import MyUserCreationForm

# Create your views here.
def home(request):
    user = User.objects.all()
    shows = Show.objects.all()
    productions = Production.objects.all()
    context = {'user': user,'shows': shows, 'productions': productions}
    # context = {}
    return render(request, 'stream/home.html', context)

# @login_required(login_url='login')
def show(request, pk):
    show=Show.objects.get(id=pk)
    # production = Production.objects.get()
    context = {'show': show}
    return render(request, 'stream/show.html', context)



def watchlist(request):
    watchlist = Watchlist.objects.all()
    context = {'watchlist': watchlist}

    return render(request, 'stream/watchlist.html', context)


def production(request, pk):
    production=Production.objects.get(id=pk)
    context = {'production': production}
    return render(request, 'stream/production.html', context)