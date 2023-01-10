from django.contrib import admin
from django.urls import path
from .views import signupfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
]