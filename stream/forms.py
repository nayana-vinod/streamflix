from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import UserDetails

from stream import models


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'email','password1', 'password2', 'bio', 'phno', 'age']

class UserForm(ModelForm):
    class Meta:
        model = UserDetails
        # fields = ['avatar', 'name', 'username', 'email', 'bio']
        fields = ['name', 'email', 'bio']