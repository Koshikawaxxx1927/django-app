# Generated by Django 4.1 on 2023-01-30 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=50, unique=True)),
                ('author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('sentence', models.TextField()),
                ('set_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='word_quiz_app.quizsetmodel')),
            ],
        ),
    ]