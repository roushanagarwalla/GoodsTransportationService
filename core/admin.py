import imp
from django.contrib import admin
from .models import Dealer, Driver, Book

# Register your models here.
admin.site.register(Dealer)
admin.site.register(Driver)
admin.site.register(Book)