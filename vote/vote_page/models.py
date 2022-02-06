from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


class Question(models.Model):
    title = models.CharField(max_length=4096)
    date = models.DateField('Date', default=date.today)
    unvisible = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail_question', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name='choice_f')
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.DO_NOTHING, related_name='answer_question')
    choice = models.ForeignKey(
        Choice, on_delete=models.DO_NOTHING, related_name='answer_choiсe')
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='user')

    def __str__(self):
        return self.choice.title
