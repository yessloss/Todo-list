from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from todolist_project.models import Task


class Index(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "todolist_project/index.html"
