from django.contrib import admin
from .models import Client
from .models import Pet

admin.site.register(Client)
admin.site.register(Pet)