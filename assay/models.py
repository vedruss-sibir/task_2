from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name


class Question(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=400)
    truth = models.BooleanField()
    votes_true = models.IntegerField(default=0)

    def __str__(self):
        return self.answer
