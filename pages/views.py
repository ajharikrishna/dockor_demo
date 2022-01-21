from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

name1 = 'before ammend'

add = 'forgotten line'


def home_page_view(request):
    name = 'hello'
    return HttpResponse('Hello WOrld')

def home__page_view_sec(request):
    name= 'hello world'
    name2 = 'my name is harikrishna'
    return HttpResponse(name , '  ', name2)