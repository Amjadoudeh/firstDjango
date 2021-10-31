from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("just")


def Amjad(request):
    return HttpResponse("Hello Amjad!")
