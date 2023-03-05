from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django import forms

from .forms import AnswerForm
from .models import Group, Question, Test, Answer


def index(request):
    group = Group.objects.all
    context = {"group": group}
    return render(request, "assay/index.html", context)


def group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    test = Test.objects.all().filter(group=group_id)
    context = {"group": group, "test": test}
    return render(request, "assay/group.html", context)


def choice(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.all().filter(test=test)
    votes_true = 0
    votes_fals = 0
    question = questions[0]
    answers = Answer.objects.all().filter(question=question)
    form = AnswerForm(question=question)
    if request.method == "POST":
        value = request.POST
        answer = value.get("answer")
        answerss = get_object_or_404(Answer, id=answer)
        if answerss.truth == True:
            votes_true = +1
        else:
            votes_fals = +1
        print("votes_true", votes_true)
        print("votes_fals", votes_fals)
    context = {"test": test, "question": question, "answer": answers, "form": form}
    return render(request, "assay/test.html", context)
