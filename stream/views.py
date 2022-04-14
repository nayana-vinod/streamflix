from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import request, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Show, Production, Watchlist
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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

@login_required(login_url='login')
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

# def watchlistAdd(request, pk):
#     show = Show.objects.get(id=pk)
    
def watchlistAdd(request, pk):
    show_to_save = get_object_or_404(Show, pk=pk)
    # Check if the item already exists in that user watchlist
    if Watchlist.objects.filter(user=request.user, id=pk).exists():
        # messages.add_message(request, messages.ERROR, "You already have it in your watchlist.")
        messages.error(request, 'You already have it in your watchlist.')
        return redirect(request, "stream/watchlist.html")
    # Get the user watchlist or create it if it doesn't exists
    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    # Add the item through the ManyToManyField (Watchlist => item)
    user_list.show.add(show_to_save)
    messages.add_message(request, messages.SUCCESS, "Successfully added to your watchlist")
    return render(request, "stream/watchlist.html")

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User doesn\'t exist.')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login(request, user, 'django.contrib.auth.backends.ModelBackend')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password doesn\'t exist')
    
    context = {}
    return render(request, 'stream/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')