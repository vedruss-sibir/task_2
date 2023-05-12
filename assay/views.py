from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import AnswerForm, CreationForm
from .models import Group, Question, Test, Answer


question_index = 0
votes_true = 0


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/signup.html"


@login_required
def index(request):
    group = Group.objects.all
    user = request.user
    context = {"group": group, "user": user}
    return render(request, "assay/index.html", context)


def group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    test = Test.objects.all().filter(group=group_id)
    context = {"group": group, "test": test}
    return render(request, "assay/group.html", context)


def choice(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    request.session["test"] = test.test_name
    questions = Question.objects.all().filter(test=test)
    global question_index, votes_true
    print("question_index", question_index)
    question = questions[question_index]
    answers = Answer.objects.all().filter(question=question)
    form = AnswerForm(question=question)
    if request.method == "POST":
        value = request.POST
        answer = value.get("answer")
        print(answer, "answer")
        if not answer:
            raise forms.ValidationError("Выбирете один вариант ответа")
        answerss = get_object_or_404(Answer, id=answer)
        question_index += 1
        if answerss.truth == True:
            votes_true += 1
        if question_index < len(questions):
            question = questions[question_index]
            answers = Answer.objects.all().filter(question=question)
            form = AnswerForm(question=question)
        if question_index == len(questions):
            question_index = 0
            if votes_true == 0:
                rezult = 0
                request.session["rezult"] = rezult
                return redirect("rezult")
            else:
                rezult = round((votes_true / len(questions) * 100), 0)
                request.session["rezult"] = rezult
                votes_true = 0
                return redirect("rezult")
    context = {"test": test, "question": question, "answer": answers, "form": form}
    return render(request, "assay/test.html", context)


def rezults(request):
    rezult = request.session.get("rezult", None)
    test = request.session.get("test", None)
    user = request.user
    context = {"user": user, "rezult": rezult, "test": test}
    return render(request, "assay/rezult.html", context)
