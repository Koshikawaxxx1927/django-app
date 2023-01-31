from django.db import models

# Create your models here.

class QuizSetModel(models.Model):

    set_name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.set_name

class QuizModel(models.Model):

    word = models.CharField(max_length=50)
    sentence = models.TextField()
    set_name = models.ForeignKey(QuizSetModel, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.word