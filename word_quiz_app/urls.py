from django.contrib import admin
from django.urls import path
from .views import signupfunc, loginfunc, listfunc, detailfunc, logoutfunc, edit_quiz, edit_quizsets, delete_quiz, delete_quizset, create_quiz, create_quizset

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
    path('logout/', logoutfunc, name='logout'),
    path('edit_quiz/<int:pk>/', edit_quiz.as_view(), name='edit_quiz'),
    path('edit_quizsets/', edit_quizsets.as_view(), name='edit_quizsets'),
    path('delete_quiz/<int:pk>/', delete_quiz.as_view(), name='delete_quiz'),
    path('delete_quizset/<int:pk>', delete_quizset.as_view(), name='delete_quizset'),
    path('create_quiz/', create_quiz.as_view(), name='create_quiz'),
    path('create_quizset/', create_quizset.as_view(), name='create_quizset'),
]