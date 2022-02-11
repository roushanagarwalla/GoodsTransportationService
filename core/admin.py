import imp
from django.contrib import admin
from .models import Dealer, Driver

# Register your models here.
admin.site.register(Dealer)
admin.site.register(Driver)