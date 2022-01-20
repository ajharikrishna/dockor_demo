from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page_view(request):
    return HttpResponse('Hello WOrld')

def home__page_view_sec(request):
    name= 'hello world'
    name2 = 'my name is harikrishna'
    return HttpResponse(name , '  ', name2)