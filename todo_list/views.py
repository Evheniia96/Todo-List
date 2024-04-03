from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


class IndexView(generic.ListView):
    # queryset = Task.objects.prefetch_related("tags")
    model = Task
    template_name = "todo_list/index.html"
    context_object_name = "task_list"


class TaskCreateView(generic.CreateView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):

    model = Task
    success_url = reverse_lazy("todo_list:index")

class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tags_list.html"


