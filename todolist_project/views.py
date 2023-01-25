from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todolist_project.models import Task, Tag


class Index(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "todolist_project/index.html"


class IndexCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todolist_project/index_form.html"
    success_url = reverse_lazy("todolist_project:index")


class IndexUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todolist_project/index_form.html"
    success_url = reverse_lazy("todolist_project:index")


class IndexDeleteView(generic.DeleteView):
    model = Task
    template_name = "todolist_project/index_confirm_delete.html"
    success_url = reverse_lazy("todolist_project:index")


class TagsListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "todolist_project/tag.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:tag_list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:tag_list")


class TagsDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todolist_project:tag_list")