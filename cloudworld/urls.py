from django.urls import path
from cloudworld import  views

urlpatterns = [
    path('',views.index)
]