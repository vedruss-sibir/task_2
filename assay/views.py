from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Group, Question, Choice


def index(request):
    group = Group.objects.all
    context = {"group": group}
    return render(request, "assay/index.html", context)


def group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    context = {
        "group": group,
    }
    return render(request, "assay/group.html", context)
