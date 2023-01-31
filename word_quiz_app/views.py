from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import QuizModel, QuizSetModel

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'signup.html', {'message': 'このユーザーはすでに登録されています。'})
        return redirect('login')
    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'message': 'ユーザー名またはパスワードが間違っています。'})
    return render(request, 'login.html', {})

@login_required
def listfunc(request):
    quiz_set = QuizSetModel.objects.filter(author=request.user).all()
    return render(request, 'list.html', {'quiz_set': quiz_set})

@login_required
def detailfunc(request, pk):
    quiz_set = get_object_or_404(QuizSetModel, pk=pk, author=request.user)
    quiz = QuizModel.objects.filter(set_name=quiz_set.id, set_name__author=request.user).all()
    return render(request, 'detail.html', {'quiz_set': quiz_set, 'quiz': quiz})
