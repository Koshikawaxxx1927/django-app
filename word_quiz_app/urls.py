from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, detailfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
]