from django.shortcuts import render
from django.http import HttpResponse
from .models import Owner, HelloKitty

# Create your views here.
def index(self):
    return HttpResponse("You are at the home page")

def human(self):
    return HttpResponse("Hello Kitty")

def cat(self):
    return HttpResponse("Hello Owner")
