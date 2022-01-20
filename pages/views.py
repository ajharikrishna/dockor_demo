from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    name = 'hello'
    return HttpResponse('Hello WOrld')

def home__page_view_sec(request):
    return HttpResponse('Hello Harikrishna')