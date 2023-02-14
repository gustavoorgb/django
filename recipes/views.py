# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('home')


def sobre(request):
    return HttpResponse('sobre')


def contato(request):
    return HttpResponse('contato')
