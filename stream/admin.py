from django.contrib import admin
# from .models import User, Production, Show, UserDetails, Plan
from .models import Production, Show, Plan, Watchlist

# Register your models here.
# admin.site.register(User)
admin.site.register(Production)
admin.site.register(Show)
admin.site.register(Plan)
admin.site.register(Watchlist)
# admin.site.register(UserDetails)