from unicodedata import name
from django.urls import path
from .views import home_page_view, home__page_view_sec

master = 'master only'

urlpatterns = [
    path('',home_page_view, name='home'),
    path('sec/', home__page_view_sec, name='sec')
]
