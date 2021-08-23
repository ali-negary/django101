from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("OK! We are in the polls index.")