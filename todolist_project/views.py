from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todolist_project.models import Task, Tag


class Index(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.filter("datetime").group_by("is_done")
    template_name = "todolist_project/index.html"


class IndexCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:index")


class IndexUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:index")


class IndexDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist_project:index")


class TagsListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "todolist_project/tag.html"


class TagsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:tag_list")


class TagsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("todolist_project:tag_list")


class TagsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:tag_list")