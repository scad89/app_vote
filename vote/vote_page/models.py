from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Question(models.Model):
    title = models.CharField(max_length=4096)
    date = models.DateField('Date', default=date.today)
    unvisible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name='choise')
    title = models.CharField(max_length=4096)
    enabled_choise = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name='question')
    choice = models.ForeignKey(
        Choice, on_delete=models.DO_NOTHING, related_name='choise')
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='user')

    def __str__(self):
        return self.choice.title
