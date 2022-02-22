from multiprocessing import context
from django.shortcuts import render, redirect
# from django.http import request, HttpResponse
# from .models import User
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.forms import UserCreationForm
# from .forms import MyUserCreationForm

# Create your views here.
def home(request):
    user = User.objects.all()
    context = {'user': user}
    # context = {}
    return render(request, 'stream/home.html', context)

def loginPage(request):
    # page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # username = request.POST.get('username').lower() 
        #entering email will work because we gave USERNAME_FIELD=email in models.py

        # email = request.POST.get('email').lower()
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # user = User.objects.get(email = email)
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        # user = authenticate(request, email = email, password = password)
        user = authenticate(request, username = username, password = password)


        if user is not None:
            login(request, user) #log the user in which creates a session in the database and the browser and the user is redirected to home page
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    # context ={'page': page}
    context = {}
    return render(request, 'stream/login_register.html', context)


def logoutUser(request):
    logout(request) #deletes that session token hence logouts the user
    return redirect('home')


def registerPage(request):
    #page = 'register' # not needed since register shows up in the else statement in login_register.html
    form = UserCreationForm()
    # form = MyUserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False) 
            #commit=False: save the form and freezing it in time (the register) to execute the next statement
            # we want to be able to create the user right away to get that user object
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'form': form}
    return render(request, 'stream/signup.html', context)