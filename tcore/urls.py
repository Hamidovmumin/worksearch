from django.urls import path
from tcore.views import index,search

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
]