from django.shortcuts import render

def signupfunc(request):
    return render(request, 'signup.html', {})