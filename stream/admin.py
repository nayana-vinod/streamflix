from django.contrib import admin
from .models import User, Production, Show, UserDetails, Plan

# Register your models here.
admin.site.register(User)
admin.site.register(Production)
admin.site.register(Show)
admin.site.register(Plan)
admin.site.register(UserDetails)