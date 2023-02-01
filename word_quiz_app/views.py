from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import QuizModel, QuizSetModel
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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

@login_required
def logoutfunc(request):
    logout(request)
    return redirect('login')

class edit_quiz(LoginRequiredMixin, ListView):
    template_name = 'edit_quiz.html'
    login_url = 'login'
    model = QuizSetModel
    context_object_name = 'quizes'
    def get(self, request, pk):
        quiz_set = get_object_or_404(QuizSetModel, pk=pk, author=request.user)
        quiz = QuizModel.objects.filter(set_name=quiz_set.id, set_name__author=request.user).all()
        return render(request, self.template_name, {'quiz_set': quiz_set, 'quiz': quiz})

class edit_quizsets(LoginRequiredMixin, ListView):
    template_name = 'edit_quizsets.html'
    login_url = 'login'
    context_object_name = 'quizsets'
    def get(self, request):
        queryset = QuizSetModel.objects.filter(author=request.user).all()
        return render(request, self.template_name, {self.context_object_name : queryset})

class delete_quiz(LoginRequiredMixin, DeleteView):
    template_name = 'delete_quiz.html'
    login_url = 'login'
    model = QuizModel
    success_url = reverse_lazy('list')

class delete_quizset(LoginRequiredMixin, DeleteView):
    template_name = 'delete_quizset.html'
    login_url = 'login'
    model = QuizSetModel
    success_url = reverse_lazy('list')

class create_quiz(LoginRequiredMixin, CreateView):
    template_name = 'create_quiz.html'
    login_url = 'login'
    model = QuizModel
    fields = ('word', 'sentence', 'set_name')
    success_url = reverse_lazy('list')
    def get(self, request):
        quiz_sets = QuizSetModel.objects.filter(author=request.user).all()
        return render(request, self.template_name, {'quiz_sets': quiz_sets})

class create_quizset(LoginRequiredMixin, CreateView):
    template_name = 'create_quizset.html'
    login_url = 'login'
    model = QuizSetModel
    fields = ('set_name', 'author')
    success_url = reverse_lazy('list')