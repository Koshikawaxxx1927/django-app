from django.contrib import admin
from .models import QuizModel, QuizSetModel
# Register your models here.

admin.site.register(QuizSetModel)
admin.site.register(QuizModel)